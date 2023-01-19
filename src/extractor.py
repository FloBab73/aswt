import numpy as np
from PIL import Image


def extract():
    im = Image.open("res/map.bmp")
    p = np.array(im)
    return p
