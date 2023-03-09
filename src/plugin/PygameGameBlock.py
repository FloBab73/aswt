import pygame

from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class PygameGameBlock(GameBlock):

    def __init__(self, x, y, width, height, block_type=BlockType.NONE):
        super().__init__(x, y, width, height, block_type)
        self.pygame_block = pygame.Rect(x, y, width, height)

    def position(self):
        return self.pygame_block

    def move_block(self, x, y):
        self.pygame_block = self.pygame_block.move(x, y)
        self.x += x
        self.y += y
