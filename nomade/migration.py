import importlib


class Migration:
    def __init__(self, id, name, date, down_migration=None):
        self.id = id
        self.name = name
        self.date = date
        self.down_migration = down_migration

    @staticmethod
    def load(location, file_name):
        if file_name.endswith('.py'):
            file_name = file_name[:-3]
        module = importlib.import_module(f'{location}.{file_name}')
        return Migration(
            id=module.curr_migration,
            name=module.migration_name,
            date=module.migration_date,
            down_migration=module.down_migration
        )
