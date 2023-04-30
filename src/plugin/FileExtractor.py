import numpy as np
from PIL import Image


def extract_file(path):
    image = Image.open(path)
    image = image.convert("RGB")

    array = np.array(image)

    return array
