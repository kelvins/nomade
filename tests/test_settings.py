import os
import toml

import pytest

from nomade.settings import Settings


class TestSettings:
    def test_load_invalid_yaml_path(self):
        with pytest.raises(FileNotFoundError):
            Settings.load('invalid/path.toml')

    def test_load_valid_yaml_file(self):
        file_path = os.path.join('tests', 'assets', 'pyproject.toml')
        settings = Settings.load(file_path)
        assert settings.location == os.path.join('tests', 'migrations')
        assert settings.template == os.path.join(
            'tests', 'assets', 'template.py'
        )
        assert settings.conn_str == 'sqlite:///:memory:'
        assert settings.date_fmt == '%d/%m/%Y'
        assert settings.name_fmt == '{date}_{time}_{id}_{slug}'

    def test_save_valid_toml_file(self):
        settings = Settings()
        settings.location = 'location'
        settings.name_fmt = '{date}_{time}_{id}_{slug}'
        settings.save('other.toml')
        expected_result = {
            'tool': {
                'nomade': {
                    'location': 'location',
                    'name-fmt': '{date}_{time}_{id}_{slug}',
                }
            }
        }
        assert toml.load('other.toml') == expected_result
        os.remove('other.toml')
