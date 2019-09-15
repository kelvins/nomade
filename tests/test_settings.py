import os
from unittest.mock import patch

import pytest
import toml

from nomade.settings import Settings


class TestSettings:
    def test_load_invalid_toml_path(self):
        with pytest.raises(FileNotFoundError):
            Settings.load('invalid/path.toml')

    def test_load_valid_toml_file(self):
        file_path = os.path.join('tests', 'assets', 'pyproject.toml')
        settings = Settings.load(file_path)
        assert settings.migrations == os.path.join('tests', 'migrations')
        assert settings.template == os.path.join(
            'tests', 'assets', 'template.py.j2'
        )
        assert settings.connection_string == 'sqlite:///:memory:'
        assert settings.date_format == '%d/%m/%Y'
        assert settings.name_format == '{date}_{time}_{id}_{slug}'

    def test_save_valid_toml_file(self):
        settings = Settings()
        settings.migrations = 'migrations'
        settings.name_format = '{date}_{time}_{id}_{slug}'
        settings.save('other.toml')
        expected_result = {
            'tool': {
                'nomade': {
                    'migrations': 'migrations',
                    'name-format': '{date}_{time}_{id}_{slug}',
                }
            }
        }
        assert toml.load('other.toml') == expected_result
        os.remove('other.toml')

    @patch.dict('os.environ', {'CONNECTION_STRING': 'test connection string'})
    def test_load_connection_string_from_environment_variable(self):
        file_path = os.path.join('tests', 'assets', 'pyproject.toml')
        settings = Settings.load(file_path)
        assert settings.connection_string == 'test connection string'
