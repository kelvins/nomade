import os
import pathlib
import shutil
from datetime import datetime

import click

from nomade import utils
from nomade.constants import level
from nomade.database import Database
from nomade.migration import Migration
from nomade.migrations import Migrations
from nomade.settings import Settings


class Nomad:
    def __init__(self, settings_path='.nomade.yml'):
        self.settings = Settings.load(settings_path)
        self.database = Database(self.settings.conn_str)

    @staticmethod
    def init():
        """Init a Nomade project by creating the
        directories and copying the settings files.
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        try:
            os.makedirs(os.path.join('nomade', 'migrations'))
            pathlib.Path(os.path.join('nomade', '__init__.py')).touch()
            pathlib.Path(
                os.path.join('nomade/migrations', '__init__.py')
            ).touch()
            shutil.copyfile(
                os.path.join(current_path, 'assets', '.nomade.yml'),
                os.path.join('.', '.nomade.yml'),
            )
            shutil.copyfile(
                os.path.join(current_path, 'assets', 'template.py'),
                os.path.join('nomade', 'template.py'),
            )
        except FileExistsError:
            click.secho('Error: file already exists!', fg=level.ERROR)
        else:
            click.secho('Initializing project:')
            click.secho('.', fg=level.INFO)
            click.secho('├── nomade', fg=level.INFO)
            click.secho('│   ├── template.py', fg=level.INFO)
            click.secho('│   └── migrations', fg=level.INFO)
            click.secho('└── .nomade.yml', fg=level.INFO)

    def migrate(self, name):
        """Create a new Nomade migration using the Migration class.

        Args:
            name (str): A short migration name (e.g. Create user table).
        """
        try:
            down_migration = Migrations(self.settings)[-1].id
        except IndexError:
            down_migration = ''

        migration = Migration(
            id=utils.unique_id(),
            name=name,
            date=datetime.now().strftime(self.settings.date_fmt),
            down_migration=down_migration,
        )
        migration.save(self.settings)
        click.secho(
            f'Migration "{migration.name}" '
            f'({migration.id}) successfully created!',
            fg=level.SUCCESS,
        )

    def _apply_migrations(self, steps, forward):
        migrations = Migrations(self.settings)

        max_steps = 'head'
        if not forward:
            migrations = migrations[::-1]
            max_steps = 'tail'

        try:
            steps = int(steps)
        except ValueError:
            if steps.strip().lower() == max_steps:
                steps = len(migrations)
            else:
                click.secho(f'Invalid step {steps}', fg=level.ERROR)
                return

        if steps <= 0:
            click.secho(f'Invalid step {steps}', fg=level.ERROR)
            return

        started = False
        curr_migration = self.database.migration_id
        for migration in migrations:
            if curr_migration is None:
                started = True

            if started:
                click.secho(
                    f'[{migration.id}] Applying "{migration.name}"... ',
                    nl=False
                )
                migration.upgrade()
                self.database.migration_id = migration.id
                steps -= 1
                click.secho('[DONE]', fg=level.SUCCESS)
                if steps == 0:
                    break
            elif migration.id == curr_migration:
                started = True

        if not started:
            click.secho('No migrations to be applied!', fg=level.WARNING)

    def upgrade(self, steps):
        self._apply_migrations(steps, forward=True)

    def downgrade(self, steps):
        self._apply_migrations(steps, forward=False)

    def history(self):
        curr_migration = self.database.migration_id
        migrations = Migrations(self.settings)
        for migration in migrations:
            click.secho(
                f'{migration.down_migration.rjust(8)}',
                nl=False,
                fg=level.WARNING,
            )
            click.secho(' -> ', nl=False)
            click.secho(f'{migration.id}', nl=False, fg=level.INFO)
            if migration.id == curr_migration:
                click.secho(
                    f': {migration.name} ({migration.date}) (head)',
                    fg=level.SUCCESS,
                )
            else:
                click.secho(f': {migration.name} ({migration.date})')

    def current(self):
        curr_migration = self.database.migration_id

        if curr_migration is None:
            click.secho('No migrations found!', fg=level.WARNING)
            return

        for migration in Migrations(self.settings):
            if migration.id == curr_migration:
                click.secho('(head) ', nl=False, fg=level.INFO)
                click.secho(
                    f'Migartion "{migration.name}" ({migration.id}) '
                    f'created at {migration.date}'
                )
                return

        click.secho(
            f'Migration {curr_migration} not found '
            f'in the {self.settings.location}',
            fg=level.ERROR,
        )
