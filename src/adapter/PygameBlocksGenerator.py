import numpy as np

from src.core.BlockType import BlockType
from src.core.Generator import Generator
from src.plugin import extractor
from src.plugin.PygameGameBlock import PygameGameBlock

# class PixelType(Enum):
WALL = [0, 0, 0]
ITEM_HEAL = [255, 216, 0]
PLAYER = [0, 255, 33]


class PygameBlocksGenerator(Generator):
    def generate(self):
        array = list(extractor.extract())
        gameBlocks = []
        activeBlocks = []

        for x in range(len(array)):
            for y in range(len(array[0])):
                if np.array_equal(array[x][y], WALL):
                    gameBlocks.append(PygameGameBlock(y * 20, x * 20, 20, 20, BlockType.WALL))
                elif np.array_equal(array[x][y], ITEM_HEAL):
                    gameBlocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_HEAL))
                elif np.array_equal(array[x][y], PLAYER):
                    activeBlocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.PLAYER))
        return gameBlocks, activeBlocks
