import importlib
import os
from datetime import datetime

from nomade import utils


class Migration:
    """Class responsible for dealing with Nomade migrations.

    Args:
        id (str): Migration unique ID.
        name (str): Migration name.
        date (str): Migration date (use the format from settings).
        down_migration (str): Down migration (None for the first migration).
        upgrade (function): Migration upgrade function.
        downgrade (function): Migration downgrade function.
    """
    def __init__(
        self, id, name, date, down_migration=None, upgrade=None, downgrade=None
    ):
        self.id = id
        self.name = name
        self.date = date
        self.down_migration = down_migration
        self.upgrade = upgrade
        self.downgrade = downgrade

    def __repr__(self):
        return f'<Migration(id={self.id}, down={self.down_migration})>'

    def _make_file_name(self, settings):
        """Method responsible for generating the migration file name.

        Args:
            settings (Settings): Nomade project settings.

        Returns:
            str: Return the migration file name.
        """
        date_time = datetime.now()
        file_name = settings.name_fmt.format(
            date=date_time.strftime('%Y%m%d'),
            time=date_time.strftime('%H%M%S'),
            id=self.id,
            slug=utils.slugify(self.name),
        )

        # Set the Python extension
        if not file_name.endswith('.py'):
            file_name += '.py'
        return file_name

    def save(self, settings):
        """Save a migration object as a migration file.

        Args:
            settings (Settings): Nomade project settings.
        """
        file_name = self._make_file_name(settings)
        with open(settings.template, 'r') as template_file:
            template = template_file.read()

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
    def _make_module_path(location, file_name):
        """Generate the module file path in the importlib format.

        Args:
            location (str): Module location (e.g. "nomade/migrations").
            file_name (str): Module file name (e.g. "20191010_migration").

        Returns:
            str, str: Return two strings:
            The first string corresponds to the module path, for example:
            "nomade.migrations.20191010_migration"
            The seconds string corresponds to the file path, for example:
            "nomade/migrations/20191010_migration.py"
        """
        # Remove file extension
        if file_name.endswith('.py'):
            file_name = file_name[:-3]

        module_path = '.'.join(os.path.normpath(location).split(os.sep))
        module_path += f'.{file_name}'

        file_path = os.path.join(os.getcwd(), location, f'{file_name}.py')
        return module_path, file_path

    @staticmethod
    def _load_module(module_path, file_path):
        """Dynamically load a module.

        Args:
            module_path (str): Module path in the importlib format (dot).
            file_path (str): Full module file path.

        Returns:
            module: Return the loaded module.
        """
        spec = importlib.util.spec_from_file_location(module_path, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    @classmethod
    def load(cls, location, file_name):
        """Load a migration file as a Migration object.

        Args:
            location (str): migration file location.
            file_name (str): migration file name.

        Returns:
            Migration: Return a Migration object with
            the information loaded from the module.
        """
        module_path, file_path = cls._make_module_path(location, file_name)
        module = cls._load_module(module_path, file_path)
        return Migration(
            id=module.curr_migration,
            name=module.migration_name,
            date=module.migration_date,
            down_migration=module.down_migration,
            upgrade=module.upgrade,
            downgrade=module.downgrade,
        )
