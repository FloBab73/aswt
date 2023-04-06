import numpy as np

from src.domain.BlockType import BlockType
from src.domain.Enemy import Enemy
from src.domain.GameBlock import GameBlock
from src.domain.Generator import Generator
from src.domain.Player import Player
from src.plugin import extractor


class BlocksGenerator(Generator):
    class PixelType:
        WALL = [0, 0, 0]
        ITEM_HEAL = [255, 216, 0]
        ITEM_KEY = [0, 38, 255]
        ITEM_VALUABLE = [0, 255, 255]
        PLAYER = [0, 255, 33]
        ENEMY = [255, 0, 0]
        DOOR = [64, 64, 64]

    def generate(self, path):
        array = list(extractor.extract(path))
        game_blocks = []
        enemies = []
        player = None

        # sort blocks with tags into arrays according to the colour
        for x in range(len(array)):
            for y in range(len(array[0])):
                if np.array_equal(array[x][y], self.PixelType.WALL):
                    game_blocks.append(GameBlock(y * 20, x * 20, 20, 20, BlockType.WALL))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_HEAL):
                    game_blocks.append(GameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_HEAL))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_KEY):
                    game_blocks.append(GameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_KEY))
                elif np.array_equal(array[x][y], self.PixelType.ITEM_KEY):
                    game_blocks.append(GameBlock(y * 20 + 5, x * 20 + 5, 10, 10, BlockType.ITEM_VALUABLE))
                elif np.array_equal(array[x][y], self.PixelType.DOOR):
                    game_blocks.append(GameBlock(y * 20, x * 20, 20, 20, BlockType.DOOR))
                elif np.array_equal(array[x][y], self.PixelType.ENEMY):
                    enemies.append(Enemy(y * 20 + 5, x * 20 + 5, 11, 11))
                elif np.array_equal(array[x][y], self.PixelType.PLAYER):
                    player = Player(y * 20 + 5, x * 20 + 5, 10, 10)

        game_blocks.append(GameBlock(-2, -2, 804, 2, BlockType.WALL))  # top
        game_blocks.append(GameBlock(800, -2, 2, 604, BlockType.WALL))  # right
        game_blocks.append(GameBlock(-2, 600, 804, 20, BlockType.WALL))  # bottom
        game_blocks.append(GameBlock(-2, -2, 2, 604, BlockType.WALL))  # left
        return game_blocks, enemies, player
