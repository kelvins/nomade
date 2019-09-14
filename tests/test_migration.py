import os
from datetime import datetime

import pytest

from nomade.migration import Migration
from nomade.settings import Settings


class TestMigration:
    def test_load_invalid_file_path(self):
        with pytest.raises(FileNotFoundError):
            Migration.load('invalid', 'file')

    def test_make_file_name_with_extension(self):
        settings = Settings()
        settings.name_format = '{date}_{id}_{slug}.py'
        migration = Migration('123', 'Test 1', None)
        date = datetime.now().strftime('%Y%m%d')
        expected_file_name = f'{date}_123_test_1.py'
        assert migration._make_file_name(settings) == expected_file_name

    def test_make_file_name_without_extension(self):
        settings = Settings()
        settings.name_format = '{date}_{id}_{slug}'
        migration = Migration('123', 'Test 1', None)
        date = datetime.now().strftime('%Y%m%d')
        expected_file_name = f'{date}_123_test_1.py'
        assert migration._make_file_name(settings) == expected_file_name

    def test_make_module_path_with_extension(self):
        module_path, file_path = Migration._make_module_path(
            'nomade/migrations', '2019_123_test.py'
        )
        assert module_path == 'nomade.migrations.2019_123_test'
        assert file_path.endswith('nomade/migrations/2019_123_test.py')

    def test_make_module_path_without_extension(self):
        module_path, file_path = Migration._make_module_path(
            'nomade/migrations', '2019_123_test'
        )
        assert module_path == 'nomade.migrations.2019_123_test'
        assert file_path.endswith('nomade/migrations/2019_123_test.py')

    def test_load_module_invalid_path(self):
        with pytest.raises(FileNotFoundError):
            Migration._load_module('nomade.invalid', 'nomade/invalid.py')

    def test_load_module_valid_path(self):
        from tests.migrations import migration_001

        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_path, 'migrations/migration_001.py')
        module = Migration._load_module('migrations.migration_001', file_path)
        assert module.migration_name == migration_001.migration_name
        assert module.migration_date == migration_001.migration_date
        assert module.curr_migration == migration_001.curr_migration
        assert module.down_migration == migration_001.down_migration

    def test_load_valid_file(self):
        migration = Migration.load('tests/migrations', 'migration_001')
        assert migration.id == '123'
        assert migration.name == 'Migration 001'
        assert migration.date == '01/01/2001'
        assert migration.down_migration is None

    def test_save_valid_migration(self):
        settings = Settings()
        settings.migrations = 'tests/migrations'
        settings.template = 'tests/assets/template.py.j2'
        settings.date_format = '%d/%m/%Y'
        settings.name_format = '{id}_{slug}'

        migration = Migration(
            id='789', name='Test Save', date='01/01/2020', down_migration='456'
        )
        migration.save(settings)

        migration = Migration.load('tests/migrations', '789_test_save')
        assert migration.id == '789'
        assert migration.name == 'Test Save'
        assert migration.date == '01/01/2020'
        assert migration.down_migration == '456'
        os.remove('tests/migrations/789_test_save.py')
