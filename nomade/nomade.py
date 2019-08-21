import os
import shutil
from datetime import datetime

from colorama import Fore

import utils
from settings import Settings
from migration import Migration


class Nomade:
    def __init__(self, settings_path='.nomade.yml'):
        self.settings = Settings.load(settings_path)

    @staticmethod
    def init():
        """Init a Nomade project by creating the
        directories and copying the settings files.
        """
        print(Fore.RESET + 'Creating Nomade project:')
        print(Fore.GREEN + '.')
        print('├─ nomade')
        print('│  ├─ template.py')
        print('│  └─ migrations')
        print('└─ .nomade.yml')

        os.makedirs(os.path.join('nomade', 'migrations'))
        shutil.copyfile(
            os.path.join('assets', '.nomade.yml'),
            os.path.join('.', '.nomade.yml')
        )
        shutil.copyfile(
            os.path.join('assets', 'template.py'),
            os.path.join('nomade', 'template.py')
        )

    @staticmethod
    def _sort_migrations(migrations):
        migrations_dict = {migration.down_migration: migration for migration in migrations}
        sorted_migrations = list()
        current_migration = ''
        while True:
            try:
                sorted_migrations.append(migrations_dict[current_migration])
                current_migration = sorted_migrations[-1].id
            except KeyError:
                break
        return sorted_migrations

    def _get_migrations(self):
        """Load all migrations unsorted.

        Returns:
            List with all migrations (objects).
        """
        migrations = list()
        for name in os.listdir(self.settings.location):
            try:
                migrations.append(Migration.load(self.settings.location, name))
            except AttributeError:
                pass
        return self._sort_migrations(migrations)

    def _get_latest_migration(self):
        return self._get_migrations()[-1]

    def migrate(self, name):
        """Create a new Nomade migration using the Migration class.

        Args:
            name (str): A short migration name (e.g. Create user table).
        """
        migration = Migration(
            id=utils.unique_id(),
            name=name,
            date=datetime.now().strftime(self.settings.date_fmt),
            down_migration=self._get_latest_migration().id
        )
        migration.save()

    def upgrade(self):
        raise NotImplementedError('Not implemented yet')

    def downgrade(self):
        raise NotImplementedError('Not implemented yet')

    def history(self):
        migrations = self._get_migrations()
        for migration in migrations:
            print(Fore.YELLOW + f'{migration.down_migration.rjust(8)} -> ' + Fore.CYAN + f'{migration.id}' + Fore.RESET + f': {migration.name} ({migration.date})')

    def current(self):
        raise NotImplementedError('Not implemented yet')
