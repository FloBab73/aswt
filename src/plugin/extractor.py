import numpy as np
from PIL import Image


def extract():
    im = Image.open("res/map2.bmp")
    p = np.array(im)
    return p
