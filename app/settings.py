import pathlib
import yaml


APP_NAME = 'app'

BASE_DIR = pathlib.Path(__file__).parent.parent

config_path = BASE_DIR / 'config' / (APP_NAME + '.yml')


def get_config(path):

    with open(path) as f:
        config = yaml.load(f)

    return config


config = get_config(config_path)
