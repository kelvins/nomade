import pytest

from nomade.migrations import Migrations
from nomade.settings import Settings


@pytest.fixture
def migrations():
    settings = Settings()
    settings.location = 'tests/migrations'
    settings.conn_str = 'sqlite:///:memory:'
    yield Migrations(settings)


class TestMigrations:
    def test_migrations_load_and_sort(self, migrations):
        assert len(migrations) == 2
        assert migrations[0].id == '123'
        assert migrations[1].id == '456'

    def test_migrations_upgrade(self, migrations):
        migrations.upgrade(1)
        assert migrations.database.migration_id == '123'
        migrations.upgrade(1)
        assert migrations.database.migration_id == '456'

    def test_migrations_downgrade(self, migrations):
        migrations.upgrade(10)
        assert migrations.database.migration_id == '456'
        migrations.downgrade(1)
        assert migrations.database.migration_id == '123'
        migrations.downgrade(1)
        assert migrations.database.migration_id is None
