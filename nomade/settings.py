import yaml


class Settings:
    """Load settings from a YAML file and convert keys to attributes."""

    @staticmethod
    def load(file_path):
        settings = Settings()
        with open(file_path, 'r') as yaml_file:
            for name, value in yaml.load(yaml_file).items():
                setattr(settings, name, value)
        return settings
