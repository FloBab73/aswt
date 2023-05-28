import numpy as np
from PIL import Image


class FileExtractor:
    def extract_file(self, path):
        image = Image.open(path)
        image = image.convert("RGB")

        array = np.array(image)

        return array
