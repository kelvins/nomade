import os

import pytest

from nomade.settings import Settings


class TestSettings:
    def test_load_invalid_yaml_path(self):
        with pytest.raises(FileNotFoundError):
            Settings.load('invalid/path.yml')

    def test_load_valid_yaml_file(self):
        file_path = os.path.join('tests', 'assets', '.nomade.yml')
        settings = Settings.load(file_path)
        assert settings.location == os.path.join('tests', 'migrations')
        assert settings.template == os.path.join(
            'tests', 'assets', 'template.py'
        )
        assert settings.conn_str == 'sqlite:///:memory:'
        assert settings.date_fmt == '%d/%m/%Y'
        assert settings.name_fmt == '{date}_{time}_{id}_{slug}'
