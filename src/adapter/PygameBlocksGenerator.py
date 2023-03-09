import numpy as np

from src.core.BlockType import BlockType
from src.core.Generator import Generator
from src.plugin import extractor
from src.plugin.PygameGameBlock import PygameGameBlock
from src.plugin.PygamePlayer import PygamePlayer


class PygameBlocksGenerator(Generator):
    class PixelType:
        WALL = [0, 0, 0]
        ITEM_HEAL = [255, 216, 0]
        ITEM_KEY = [0, 38, 255]
        ITEM_VALUABLE = [0, 255, 255]
        PLAYER = [0, 255, 33]
        ENEMY = [255, 0, 0]
        DOOR = [64, 64, 64]

    def generate(self):
        array = list(extractor.extract())
        game_blocks = []
        active_blocks = []

        # sort blocks with tags into arrays according to the colour
        for x in range(len(array)):
            for y in range(len(array[0])):
                if np.array_equal(array[x][y], self.PixelType.WALL):
                    game_blocks.append(PygameGameBlock(y * 20, x * 20, 20, 20, BlockType.WALL))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_HEAL):
                    game_blocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_HEAL))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_KEY):
                    game_blocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_KEY))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_KEY):
                    game_blocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_VALUABLE))
                elif np.array_equal(array[x][y], self.PixelType.DOOR):
                    game_blocks.append(PygameGameBlock(y * 20, x * 20 - 20, 20, 40, BlockType.DOOR))
                elif np.array_equal(array[x][y], self.PixelType.ENEMY):
                    active_blocks.append(PygameGameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ENEMY))
                elif np.array_equal(array[x][y], self.PixelType.PLAYER):
                    active_blocks.append(PygamePlayer(y * 20 + 5, x * 20 + 5, 10, 10))

        game_blocks.append(PygameGameBlock(-2, -2, 804, 2, BlockType.WALL))
        game_blocks.append(PygameGameBlock(800, -2, 2, 604, BlockType.WALL))
        game_blocks.append(PygameGameBlock(-2, 600, 804, 2, BlockType.WALL))
        game_blocks.append(PygameGameBlock(-2, -2, 2, 604, BlockType.WALL))
        return game_blocks, active_blocks
