
import os
import configparser


import keras

if int(keras.__version__.split('.')[0]) < 2:
    raise ImportError('You need keras version 2.0.0 or higher. Run "pip install keras --upgrade"')

config = configparser.ConfigParser()

my_path = os.path.expanduser('~/mydonkey/')
sessions_path = os.path.join(my_path, 'sessions')
models_path = os.path.join(my_path, 'models')
datasets_path = os.path.join(my_path, 'datasets')
results_path = os.path.join(my_path, 'results')


def parse_config(config_path):
    config_path = os.path.expanduser(config_path)
    config.read(config_path)

    cfg={}

    pilot = config['pilot']
    cfg['pilot_model_path'] = os.path.expanduser(pilot.get('model_path'))

    return cfg
