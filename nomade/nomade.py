import os
import shutil
from datetime import datetime

import log
import utils
from settings import Settings
from migration import Migration
from database import Database


class Nomade:
    def __init__(self, settings_path='.nomade.yml'):
        self.settings = Settings.load(settings_path)

    @staticmethod
    def init():
        """Init a Nomade project by creating the
        directories and copying the settings files.
        """
        try:
            os.makedirs(os.path.join('nomade', 'migrations'))
            shutil.copyfile(
                os.path.join('assets', '.nomade.yml'),
                os.path.join('.', '.nomade.yml')
            )
            shutil.copyfile(
                os.path.join('assets', 'template.py'),
                os.path.join('nomade', 'template.py')
            )
        except FileExistsError:
            log.error('Error: file already exists!')
        else:
            log.default('Initializing project:')
            log.success('.')
            log.success('├─ nomade')
            log.success('│  ├─ template.py')
            log.success('│  └─ migrations')
            log.success('└─ .nomade.yml')

    def migrate(self, name):
        """Create a new Nomade migration using the Migration class.

        Args:
            name (str): A short migration name (e.g. Create user table).
        """
        try:
            down_migration = Migration.get_migrations(self.settings)[-1]
        except IndexError:
            down_migration = ''

        migration = Migration(
            id=utils.unique_id(),
            name=name,
            date=datetime.now().strftime(self.settings.date_fmt),
            down_migration=down_migration
        )
        migration.save(self.settings)
        log.success(
            f'Migration ({migration.id}) {migration.name} successfully created'
        )

    def upgrade(self, steps):
        raise NotImplementedError('Not implemented yet')

    def downgrade(self, steps):
        raise NotImplementedError('Not implemented yet')

    def history(self):
        # TODO: show the current migration
        migrations = Migration.get_migrations(self.settings)
        for migration in migrations:
            log.warning(f'{migration.down_migration.rjust(8)}', end='')
            log.default(' -> ', end='')
            log.info(f'{migration.id}', end='')
            log.default(f': {migration.name} ({migration.date})')

    def current(self):
        database = Database(self.settings.conn_str)
        try:
            migration_id = database.read_migration().migration
        except AttributeError:
            log.error('No migrations found!')
            return

        for migration in Migration.get_migrations(self.settings):
            if migration.id == migration_id:
                log.default('Current migration:')
                log.warning(f'{migration.down_migration.rjust(8)}', end='')
                log.default(' -> ', end='')
                log.info(f'{migration.id}', end='')
                log.default(f': {migration.name} ({migration.date})')
