import os

import toml


class Settings:
    """Settings class responsible for dealing with TOML files."""

    def save(self, file_path='pyproject.toml'):
        """Dump the current settings to a TOML file.

        Args:
            file_path (str): path to the TOML file.

        Returns:
            str: A string containing the TOML-formatted
            data corresponding to current object.
        """
        content = {'tool': {'nomade': None}}
        content['tool']['nomade'] = {
            k.replace('_', '-'): v for k, v in self.__dict__.items()
        }
        with open(file_path, 'a') as f:
            return toml.dump(content, f)

    @staticmethod
    def load(file_path='pyproject.toml'):
        """Factory method responsible for loading settings
        from a TOML file.

        Args:
            file_path (str): path to the TOML file.

        Returns:
            Settings: Return a Settings object with the
            attributes loaded from the TOML file.
        """
        content = toml.load(file_path)
        settings = Settings()
        for key, value in content['tool']['nomade'].items():
            setattr(settings, key.replace('-', '_'), value)

        if 'CONNECTION_STRING' in os.environ:
            setattr(
                settings, 'connection_string', os.environ['CONNECTION_STRING']
            )

        return settings
