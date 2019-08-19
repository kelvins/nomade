import yaml


class Settings:
    """Load settings from a YAML file and convert keys to attributes."""

    @staticmethod
    def load(file_path):
        settings = Settings()
        with open(file_path, 'r') as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            for name, value in data.items():
                setattr(settings, name, value)
        return settings
