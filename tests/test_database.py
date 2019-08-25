import pytest
import sqlalchemy as sa

from nomade.database import Database, Nomade


class TestDatabase:
    def test_database_invalid_connection_string_value_error(self):
        with pytest.raises(ValueError):
            Database('sqlite://invalid:path')

    def test_database_invalid_connection_string_argument_error(self):
        with pytest.raises(sa.exc.ArgumentError):
            Database('database:invalid:path')

    def test_database_save_and_read_migration(self):
        database = Database('sqlite:///:memory:')
        assert database.read_migration() == None
        database.save_migration('test123')
        assert database.read_migration().migration == 'test123'
