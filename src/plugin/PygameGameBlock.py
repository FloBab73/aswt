import pygame

from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class PygameGameBlock(GameBlock):
    NON = BlockType.NON
    WALL = BlockType.WALL
    SECRET = BlockType.SECRET
    ITEM = BlockType.ITEM

    def __init__(self, x, y, width, height, blockType=BlockType.NON):
        super().__init__(x, y, width, height, blockType)
        self.pygameBlock = pygame.Rect(x, y, width, height)
