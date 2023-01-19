import numpy as np
from PIL import Image


def extract():
    image = Image.open("res/map2.bmp")
    array = np.array(image)
    return array
