from nomade.migration import Migration
from nomade.migrations import Migrations
from nomade.settings import Settings


class TestMigrations:
    def test_migrations(self):
        settings = Settings()
        settings.location = 'tests/migrations'
        settings.conn_str = 'sqlite:///test_migrations.db'
        migrations = Migrations(settings)
        assert len(migrations) == 2
        assert migrations[0].id == '123'
        assert migrations[1].id == '456'
