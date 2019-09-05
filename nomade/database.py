from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = sa.orm.sessionmaker(expire_on_commit=False)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


class NomadeModel(Base):
    """Nomade model class representing the nomade
    table that will be stored in the database.
    """

    __tablename__ = 'nomade'
    migration = sa.Column(sa.String, primary_key=True)

    def __repr__(self):
        return f'<Nomade(migration={self.migration})>'


class Database:
    """Class responsible for dealing with simple database operations.
    (e.g. get migration ID, set current migration ID).
    """

    def __init__(self, connection_string):
        engine = sa.create_engine(connection_string)
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)

    def _nomade_model(self):
        """Get the current migration from the database.

        Returns:
            NomadeModel: Return the NomadeModel object representing
            the migration from the database, if no migration was found
            return a new NomadeModel object.
        """
        with session_scope() as session:
            return session.query(NomadeModel).first() or NomadeModel()

    @property
    def migration_id(self):
        """Get the current migration ID.

        Returns:
            str: Return the current migration ID.
            Return None if no record was found.
        """
        return self._nomade_model().migration or None

    @migration_id.setter
    def migration_id(self, id):
        """Insert or Update the current model ID in the database.

        Args:
            id (str): Migration ID do be saved in the database.
        """
        nomade_model = self._nomade_model()
        nomade_model.migration = id
        with session_scope() as session:
            if nomade_model.migration:
                session.add(nomade_model)
            else:
                try:
                    session.delete(nomade_model)
                except sa.exc.InvalidRequestError:
                    pass
