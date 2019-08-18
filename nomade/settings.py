import yaml


class Settings:
    """Load settings from a YAML file and convert keys to attributes."""
    def __init__(self, file_path):
        self.load(file_path)

    def load(self, file_path):
        with open(file_path, 'r') as f:
            settings = yaml.load(f)
        for name, value in settings.items():
            setattr(self, name, value)
