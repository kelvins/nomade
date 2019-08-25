import os
import shutil

import pytest

from nomade.migration import Migration
from nomade.settings import Settings


class TestMigration:
    @classmethod
    def setup_class(cls):
        os.mkdir(os.path.join('tests', 'migrations'))

    @classmethod
    def teardown_class(cls):
        shutil.rmtree('tests/migrations')

    def test_load_invalid_file_path(self):
        with pytest.raises(FileNotFoundError):
            Migration.load('invalid', 'file')

    def test_load_valid_file(self):
        migration = Migration.load('tests/assets', 'migration_001')
        assert migration.id == 'R2D2'
        assert migration.name == 'Migration 001'
        assert migration.date == '01/01/2001'
        assert migration.down_migration == 'C3PO'

    def test_save_valid_migration(self):
        settings = Settings()
        settings.location = 'tests/migrations'
        settings.template = 'tests/assets/template.py'
        settings.date_fmt = '%d/%m/%Y'
        settings.name_fmt = '{id}_{slug}'

        migration = Migration(
            id='456', name='Test Save', date='01/01/2020', down_migration='123'
        )
        migration.save(settings)

        migration = Migration.load('tests/migrations', '456_test_save')
        assert migration.id == '456'
        assert migration.name == 'Test Save'
        assert migration.date == '01/01/2020'
        assert migration.down_migration == '123'
