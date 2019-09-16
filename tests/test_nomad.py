import os
from datetime import datetime
from unittest.mock import Mock, patch

import click
import pytest

from nomade.migrations import Migrations
from nomade.nomad import Nomad
from nomade.settings import Settings


@pytest.fixture
def nomad():
    yield Nomad(os.path.join('tests', 'assets', 'pyproject.toml'))


class TestNomad:
    def teardown_method(self, method):
        for file_name in os.listdir(os.path.join('tests', 'migrations')):
            if file_name.endswith('_create_table.py'):
                os.remove(os.path.join('tests', 'migrations', file_name))

    @patch('shutil.copyfile')
    def test_init(self, copyfile, monkeypatch):
        makedirs = Mock(side_effect=FileExistsError('File already exists'))
        monkeypatch.setattr(os, 'makedirs', makedirs)
        monkeypatch.setattr(Settings, 'save', Mock())
        Nomad.init()
        makedirs.assert_called_once_with(os.path.join('nomade', 'migrations'))
        copyfile.assert_called_once()

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

    def test_stamp(self, nomad, monkeypatch):
        nomad.migrate('Create table')
        migration = Migrations(nomad.settings)[-1]
        monkeypatch.setattr(migration, 'upgrade', Mock())
        monkeypatch.setattr(migration, 'downgrade', Mock())

        assert nomad.database.migration_id is None
        nomad.stamp(migration.id)
        assert nomad.database.migration_id == migration.id
        migration.upgrade.assert_not_called()
        migration.downgrade.assert_not_called()

    def test_upgrade_with_head(self, nomad, monkeypatch):
        upgrade = Mock()
        monkeypatch.setattr(Migrations, 'upgrade', upgrade)
        nomad.upgrade('head')
        upgrade.assert_called_once_with(2)

    def test_downgrade_with_tail(self, nomad, monkeypatch):
        downgrade = Mock()
        monkeypatch.setattr(Migrations, 'downgrade', downgrade)
        nomad.downgrade('tail')
        downgrade.assert_called_once_with(2)

    def test_current_no_migration(self, nomad, monkeypatch):
        monkeypatch.setattr(click, 'secho', Mock())
        nomad.current()
        assert click.secho.call_count == 1

    def test_current_with_valid_migration(self, nomad, monkeypatch):
        nomad.upgrade('1')
        monkeypatch.setattr(click, 'secho', Mock())
        nomad.current()
        assert click.secho.call_count == 4

    def test_current_invalid_migration(self, nomad, monkeypatch):
        monkeypatch.setattr(click, 'secho', Mock())
        nomad.database.migration_id = 'invalid migration id'
        nomad.current()
        assert click.secho.call_count == 1

    def test_stamp_invalid_migration_id(self, nomad, monkeypatch):
        monkeypatch.setattr(click, 'secho', Mock())
        nomad.stamp('invalid migration id')
        assert click.secho.call_count == 1
        assert nomad.database.migration_id is None

    def test_stamp_valid_migration_id(self, nomad, monkeypatch):
        monkeypatch.setattr(click, 'secho', Mock())
        nomad.stamp('456')
        assert click.secho.call_count == 3
        assert nomad.database.migration_id == '456'
