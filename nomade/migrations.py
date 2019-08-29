import functools
import os
import pkgutil

import click

from nomade.constants import level
from nomade.database import Database
from nomade.migration import Migration


class Migrations:
    """Class responsible for loading the migrations sorted.

    Args:
        settings (Settings): A settings object with migrations location.
    """
    def __init__(self, settings):
        self.settings = settings
        self.database = Database(self.settings.conn_str)
        self._migrations = self._load(self.settings)
        self.sort()

    def __getitem__(self, index):
        return self._migrations[index]

    def __len__(self):
        return len(self._migrations)

    def sort(self):
        """Sort the _migrations list based on the migration ID."""
        migrations_dict = {m.down_migration: m for m in self._migrations}
        self._migrations = list()
        current = ''
        while True:
            try:
                self._migrations.append(migrations_dict[current])
                current = self._migrations[-1].id
            except KeyError:
                break

    @staticmethod
    def _load(settings):
        """Load all migrations based on the settings location.

        Args:
            settings (Settings): A settings object with migrations location.

        Returns:
            list: Return a list of Migration objects unsorted.
        """
        migrations = list()
        path = os.path.join(os.getcwd(), settings.location)
        modules = pkgutil.iter_modules(path=[path])
        for _, name, _ in modules:
            try:
                migrations.append(Migration.load(settings.location, name))
            except AttributeError:
                pass
        return migrations

    def apply_migrations(func):
        @functools.wraps(func)
        def wrapper(self, steps):
            if steps <= 0:
                click.secho('Error: invalid step value', fg=level.ERROR)
                return

            migrations_applied = False
            for migration in func(self, steps):
                click.secho(f'Applying {func.__name__} migration "', nl=False)
                click.secho(f'{migration.name}', nl=False, fg=level.INFO)
                click.secho(f'" ({migration.id})... ', nl=False)
                migrations_applied = True

            if not migrations_applied:
                click.secho('No migrations to apply!', fg=level.WARNING)
        return wrapper

    @apply_migrations
    def upgrade(self, steps):
        """Upgrade migrations based on steps.

        Args:
            steps (int): the number of steps do upgrade.

        Return:
            bool: Return a flag stating if migrations have been applied.
        """
        migration_id = self.database.migration_id
        init_migrations = not bool(migration_id)

        for migration in self:
            # Found the current migration, let's apply the next one
            if migration.id == migration_id:
                init_migrations = True
                continue

            if init_migrations:
                yield migration
                migration.upgrade()
                self.database.migration_id = migration.id
                click.secho('[DONE]', fg=level.SUCCESS)

                steps -= 1
                if steps == 0:
                    break

    @apply_migrations
    def downgrade(self, steps):
        """Downgrade migrations based on steps.

        Args:
            steps (int): the number of steps do downgrade.

        Return:
            bool: Return a flag stating if migrations have been applied.
        """
        migration_id = self.database.migration_id
        init_migrations = not bool(migration_id)

        # Run migrations in reverse order for downgrade
        for migration in self[::-1]:
            if migration.id == migration_id:
                init_migrations = True

            if init_migrations:
                yield migration
                migration.downgrade()
                self.database.migration_id = migration.down_migration
                click.secho('[DONE]', fg=level.SUCCESS)

                steps -= 1
                if steps == 0:
                    break
