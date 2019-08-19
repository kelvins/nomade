import os
import uuid
import shutil
from datetime import datetime
from functools import namedtuple

import utils
from settings import Settings

Migration = namedtuple(
    'Migration', ('id', 'name', 'date', 'up_migration', 'down_migration')
)


class Nomade:
    def __init__(self, settings_path='.nomade.yml'):
        self.settings = Settings.load(settings_path)

    @staticmethod
    def init(location='.'):
        os.mkdir('migrations')
        files_to_copy = ['.nomade.yml', 'template.py']
        for file in files_to_copy:
            shutil.copyfile(
                os.path.join('assets', file),
                os.path.join(location, file)
            )

    def migrate(self, name):
        # Generate migration parameters
        unique_id = str(uuid.uuid4())[:10]
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
            name=name,
            date=date_time.strftime(self.settings.date_fmt),
            up_migration=unique_id,
            down_migration=None  # TODO: retrieve current migration from files
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
        raise NotImplementedError('Not implemented yet')

    def current(self):
        raise NotImplementedError('Not implemented yet')
