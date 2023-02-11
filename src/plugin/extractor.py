import numpy as np
from PIL import Image


def extract():
    image = Image.open("res/map3.bmp")
    image = image.convert("RGB")

    array = np.array(image)

    return array
