import yaml


class Settings:
    """Settings class responsible for dealing with YAML files."""

    @staticmethod
    def load(path):
        """Load the settings from a YAML file.

        Args:
            path (str): path for the YAML file.

        Returns:
            Return a Settings object with the attributes
            from the YAML file.
        """
        with open(path, 'r') as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)

        settings = Settings()
        for key, value in data.items():
            setattr(settings, key, value)
        return settings
