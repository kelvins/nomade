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


class Nomade(Base):
    __tablename__ = 'nomade'
    migration = sa.Column(sa.String, primary_key=True)

    def __repr__(self):
        return f'<Nomade(migration={self.migration})>'


class Database:
    def __init__(self, connection_string):
        self.engine = sa.create_engine(connection_string)
        Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def read_migration(self):
        with session_scope() as session:
            return session.query(Nomade).first()

    def save_migration(self, migration_id):
        nomade = self.read_migration() or Nomade()
        nomade.migration = migration_id
        with session_scope() as session:
            session.add(nomade)
