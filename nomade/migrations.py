import os
import pkgutil

from nomade.migration import Migration


class Migrations:
    """Class responsible for loading the migrations sorted.

    Args:
        settings (Settings): A settings object with migrations location.
    """
    def __init__(self, settings):
        self.settings = settings
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
