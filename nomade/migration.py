import os
import importlib
from datetime import datetime

from nomade import utils


class Migration:
    def __init__(self, id, name, date, down_migration=None):
        self.id = id
        self.name = name
        self.date = date
        self.down_migration = down_migration
        self.upgrade = None
        self.downgrade = None

    def __repr__(self):
        return f'<Migration id={self.id}, down={self.down_migration}>'

    def save(self, settings):
        """Save a migration object as a migration file.

        Args:
            settings (Settings): A settings object.
        """
        date_time = datetime.now()
        file_name = settings.name_fmt.format(
            date=date_time.strftime('%Y%m%d'),
            time=date_time.strftime('%H%M%S'),
            id=self.id,
            slug=utils.slugify(self.name),
        )

        # Add Python extension to the file name
        if not file_name.endswith('.py'):
            file_name += '.py'

        with open(settings.template, 'r') as template_file:
            template = template_file.read()

        # TODO: for more complex templates we can use jinja2
        file_content = template.format(
            migration_name=self.name,
            migration_date=self.date,
            curr_migration=self.id,
            down_migration=self.down_migration or '',
        )

        file_path = os.path.join(settings.location, file_name)
        with open(file_path, 'w') as migration_file:
            migration_file.write(file_content)

    @staticmethod
    def load(location, file_name):
        """Load a migration file as a Migration object.

        Args:
            location (str): migration file location.
            file_name (str): migration file name.

        Returns:
            Return a Migration object containing the migration info.
        """
        # importlib requires location splitted by dot
        location = '.'.join(os.path.normpath(location).split(os.sep))

        # If the file name came with the file extension, remove it
        if file_name.endswith('.py'):
            file_name = file_name[:-3]

        module = importlib.import_module(f'{location}.{file_name}')
        return Migration(
            id=module.curr_migration,
            name=module.migration_name,
            date=module.migration_date,
            down_migration=module.down_migration or None,
            upgrade=module.upgrade,
            downgrade=module.downgrade,
        )

    @staticmethod
    def _sort_migrations(migrations):
        migrations_dict = {m.down_migration: m for m in migrations}
        migrations = list()
        current = ''
        while True:
            try:
                migrations.append(migrations_dict[current])
                current = migrations[-1].id
            except KeyError:
                break
        return migrations

    @classmethod
    def get_migrations(cls, settings):
        migrations = list()
        for name in os.listdir(settings.location):
            try:
                migrations.append(Migration.load(settings.location, name))
            except AttributeError:
                pass
        return cls._sort_migrations(migrations)
