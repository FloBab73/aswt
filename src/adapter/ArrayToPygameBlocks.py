import numpy as np

from src.core.Generator import Generator
from src.plugin import extractor
from src.plugin.GameBlock import GameBlock

wall = [0, 0, 0]
item = [255, 216, 0]


class ArrayToPygameBlocks(Generator):
    def generate(self):
        array = list(extractor.extract())
        result = []

        for x in range(len(array)):
            for y in range(len(array[0])):
                if np.array_equal(array[x][y], wall):
                    result.append(GameBlock(y * 20, x * 20, 20, 20, GameBlock.WALL))
                if np.array_equal(array[x][y], item):
                    result.append(GameBlock(y * 20 + 5, x * 20 + 5, 10, 10, GameBlock.ITEM))
        return result
