import sqlalchemy as sa

Base = sa.ext.declarative.declarative_base()
Session = sa.orm.sessionmaker()


class Nomade(Base):
    __tablename__ = 'nomade'
    migration = sa.Column(sa.String)

    def __repr__(self):
        return f'<Nomade(migration={migration})>'


class Database:
    def __init__(self, connection_string):
        self.engine = sa.create_engine(connection_string)
        Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def read_migration(self):
        session = Session()
        with session.begin():
            return session.query(Nomade).first()

    def save_migration(self, migration_id):
        nomade = self.read_migration() or Nomade()
        nomade.migration = migration_id
        session = Session()
        with session.begin():
            session.add(nomade)
