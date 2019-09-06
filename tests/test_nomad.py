import os
from datetime import datetime
from unittest import mock

import pytest

from nomade.migrations import Migrations
from nomade.nomad import Nomad


@pytest.fixture
def nomad():
    yield Nomad(os.path.join('tests', 'assets', '.nomade.yml'))


class TestNomad:
    @mock.patch('os.makedirs')
    @mock.patch('shutil.copyfile')
    def test_init(self, copyfile, makedirs):
        Nomad.init()
        makedirs.assert_called_once_with(os.path.join('nomade', 'migrations'))
        assert copyfile.call_count == 2

    def test_steps_to_int_with_max_steps(self):
        assert Nomad._steps_to_int('head', 'head', 5) == 5

    def test_steps_to_int_with_valid_steps(self):
        assert Nomad._steps_to_int('10', 'head', 20) == 10

    def test_steps_to_int_with_invalid_steps(self):
        assert Nomad._steps_to_int('tail', 'head', 5) == 0

    def test_migrate(self, nomad):
        nomad.migrate('Create table')
        migration = Migrations(nomad.settings)[-1]
        assert migration.name == 'Create table'
        assert migration.date == datetime.now().strftime('%d/%m/%Y')
        assert migration.down_migration == '456'
        for file_name in os.listdir(os.path.join('tests', 'migrations')):
            if file_name.endswith(f'{migration.id}_create_table.py'):
                os.remove(os.path.join('tests', 'migrations', file_name))
