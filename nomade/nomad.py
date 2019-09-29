import os
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
    def __init__(self, settings_path='pyproject.toml'):
        self.settings = Settings.load(settings_path)
        try:
            self.database = Database(self.settings.connection_string)
        except AttributeError:
            click.secho(
                'Error: CONNECTION_STRING not defined!', fg=level.ERROR
            )
            exit(1)

    @staticmethod
    def init():
        """Init a Nomade project by creating the
        directories and copying the necessary files.
        """
        try:
            os.makedirs(os.path.join('nomade', 'migrations'))
        except FileExistsError:
            pass

        current_path = os.path.dirname(os.path.abspath(__file__))

        settings = Settings.load(
            os.path.join(current_path, 'assets', 'pyproject.toml')
        )
        settings.save('pyproject.toml')

        shutil.copyfile(
            os.path.join(current_path, 'assets', 'template.py.j2'),
            os.path.join('nomade', 'template.py.j2'),
        )
        click.secho('Initializing ', nl=False)
        click.secho('Nomade', nl=False, fg=level.INFO)
        click.secho(' project:')
        click.secho('.')
        click.secho('├── nomade')
        click.secho('│   ├── template.py.j2')
        click.secho('│   └── migrations')
        click.secho('└── pyproject.toml')

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
            date=datetime.now().strftime(self.settings.date_format),
            down_migration=down_migration,
        )
        migration.save(self.settings)
        click.secho('Migration "', nl=False)
        click.secho(f'{migration.name}', nl=False, fg=level.INFO)
        click.secho(f'" ({migration.id}) successfully created!')

    @staticmethod
    def _steps_to_int(steps, keyword, max_steps):
        """Convert the steps argument to a integer value.

        Args:
            steps (str): the steps argument passed by user.
            keyword (str): the keyword 'head' or 'tail'.
            max_steps (int): the maximum number of valid migrations.

        Returns:
            int: Return the 'steps' value as integer.
            Return 0 if 'steps' is invalid.
        """
        if steps.strip().lower() == keyword:
            return max_steps
        try:
            return int(steps)
        except ValueError:
            return 0

    def upgrade(self, steps):
        """Upgrade migrations based on steps.

        Args:
            steps (str): steps may 'head' or a number.
        """
        migrations = Migrations(self.settings)
        steps = self._steps_to_int(steps, 'head', len(migrations))
        migrations.upgrade(steps)

    def downgrade(self, steps):
        """Downgrade migrations based on steps.

        Args:
            steps (str): steps may 'tail' or a number.
        """
        migrations = Migrations(self.settings)
        steps = self._steps_to_int(steps, 'tail', len(migrations))
        migrations.downgrade(steps)

    def history(self):
        """Show a list of all migrations."""
        migration_id = self.database.migration_id

        for migration in Migrations(self.settings):
            down_migration = migration.down_migration or 'Start'
            click.secho(
                f'{down_migration.rjust(8)}', nl=False, fg=level.WARNING
            )
            click.secho(' -> ', nl=False)
            click.secho(f'{migration.id}', nl=False, fg=level.INFO)
            click.secho(f': {migration.name} ({migration.date})', nl=False)

            # Show the (head) suffix to the current migration
            if migration.id == migration_id:
                click.secho(' (head)', fg=level.SUCCESS)
            else:
                click.secho('')

    def current(self):
        """Show the current migration."""
        migration_id = self.database.migration_id
        if not migration_id:
            click.secho('No migrations found!', fg=level.WARNING)
            return

        for migration in Migrations(self.settings):
            if migration.id == migration_id:
                click.secho(f'[{migration.id}] Migration "', nl=False)
                click.secho(f'{migration.name}', nl=False, fg=level.INFO)
                click.secho(f'" created at {migration.date} ', nl=False)
                click.secho('(head)', fg=level.SUCCESS)
                return

        click.secho(
            f'Migration {migration_id} not '
            f'found in {self.settings.migrations}',
            fg=level.ERROR,
        )

    def stamp(self, migration_id):
        """Stamp a specific revision to the database.

        Args:
            migration_id (str): revision ID.
        """
        for migration in Migrations(self.settings):
            if migration.id == migration_id:
                self.database.migration_id = migration.id
                click.secho(f'[{migration.id}] Migration "', nl=False)
                click.secho(f'{migration.name}', nl=False, fg=level.INFO)
                click.secho(f'" successfully stamped.')
                return
        else:
            click.secho(
                f'Migration {migration_id} not '
                f'found in {self.settings.migrations}',
                fg=level.ERROR,
            )
