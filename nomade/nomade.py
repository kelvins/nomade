import os
import uuid
import copy
import shutil
from datetime import datetime
from functools import namedtuple

from colorama import Fore

import utils
from settings import Settings
from migration import Migration


class Nomade:
    def __init__(self, settings_path='.nomade.yml'):
        self.settings = Settings.load(settings_path)

    @staticmethod
    def init():
        os.makedirs('nomade/migrations')
        shutil.copyfile(
            os.path.join('assets', '.nomade.yml'),
            os.path.join('.', '.nomade.yml')
        )
        shutil.copyfile(
            os.path.join('assets', 'template.py'),
            os.path.join('./nomade', 'template.py')
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
            if not name.startswith('__') and not name.endswith('__.py'):
                migrations.append(Migration.load(self.settings.location, name))
        return self._sort_migrations(migrations)

    def _get_latest_migration(self):
        return self._get_migrations()[-1]

    def migrate(self, name):
        # Generate migration parameters
        unique_id = utils.unique_id()
        date_time = datetime.now()
        slug = utils.slugify(name)

        # Create migration file name based on settings.name_fmt
        file_name = self.settings.name_fmt.format(
            date=date_time.strftime('%Y%m%d'),
            time=date_time.strftime('%H%M%S'),
            id=unique_id,
            slug=slug
        )
        if not file_name.endswith('.py'):
            file_name += '.py'

        # Read content from the template file
        with open(self.settings.template, 'r') as template_file:
            template = template_file.read()

        # TODO: we can use jinja2 if needed
        # Generate the file content
        file_content = template.format(
            migration_name=name,
            migration_date=date_time.strftime(self.settings.date_fmt),
            curr_migration=unique_id,
            down_migration=self._get_latest_migration().id
        )

        # Create the migration file
        file_path = os.path.join(self.settings.location, file_name)
        with open(file_path, 'w') as migration_file:
            migration_file.write(file_content)

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
