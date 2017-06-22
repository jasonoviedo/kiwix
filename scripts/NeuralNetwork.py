import donkey as dk
import os
import numpy as np
from PIL import Image
'''
Python code for booting up the Neural Network
'''

def prepare_neural_network():

    mydonkey_path = '~/mydonkey'
    mydonkey_path = os.path.expanduser(mydonkey_path)
    sessions_path = os.path.join(mydonkey_path, 'sessions')
    models_path = os.path.join(mydonkey_path, 'models')
    ph = dk.pilots.PilotHandler(models_path)

    virtual_pilot = ph.default_pilots()[0]

    #session_study = dk.sessions.Session(os.path.join(sessions_path, 'Virtual'))

    virtual_pilot.load()

    return virtual_pilot


def load_frame(file_path):
    '''
    Retrive an image with the strange encoding
    '''
    with Image.open(file_path) as img:
        img_arr = np.array(img)

    return img_arr

if __name__ == "__main__":

    virtual_pilot = prepare_neural_network()

    #img_arr = load_frame(file)

    #angle, throttle = virtual_pilot.decide(img_arr)




