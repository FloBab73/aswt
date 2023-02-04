import pygame

from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class PygameGameBlock(GameBlock):

    def __init__(self, x, y, width, height, blockType=BlockType.NON):
        super().__init__(x, y, width, height, blockType)
        self.pygameBlock = pygame.Rect(x, y, width, height)

    def position(self):
        return self.pygameBlock

    def moveBlock(self, x, y):
        self.pygameBlock = self.pygameBlock.move(x, y)
        self.x += x
        self.y += y
