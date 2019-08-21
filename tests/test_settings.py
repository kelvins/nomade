import os

import pytest

from nomade.settings import Settings


class TestSettings:

    def test_load_invalid_yaml_path(self):
        with pytest.raises(FileNotFoundError):
            Settings.load('invalid/path.yml')

    def test_load_valid_yaml_file(self):
        path = os.path.join('tests', 'assets', '.nomade.yml')
        settings = Settings.load(path)
        assert settings.location == os.path.join('nomade', 'migrations')
        assert settings.template == os.path.join('nomade', 'template.py')
        assert settings.conn_str == 'user:pass@localhost:5432/db_name'
        assert settings.date_fmt == '%d/%m/%Y'
        assert settings.name_fmt == '{date}_{time}_{id}_{slug}'
