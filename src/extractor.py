import numpy as np
from PIL import Image


def extract():
    im = Image.open("res/map1.bmp")
    p = np.array(im)
    return p
