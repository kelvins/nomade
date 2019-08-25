import yaml


class Settings:
    """Settings class responsible for dealing with YAML files."""

    @staticmethod
    def load(file_path):
        """Factory method responsible for loading settings
        from a YAML file.

        Args:
            file_path (str): path to the YAML file.

        Returns:
            Settings: Return a Settings object with the
            attributes loaded from the YAML file.
        """
        with open(file_path, 'r') as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)

        settings = Settings()
        for key, value in data.items():
            setattr(settings, key, value)
        return settings
