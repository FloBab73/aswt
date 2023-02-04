import pygame

from src.core.BlockType import BlockType


class GameBlock(pygame.Rect):
    NON = BlockType.NON
    WALL = BlockType.WALL
    SECRET = BlockType.SECRET
    ITEM = BlockType.ITEM

    def __init__(self, x, y, width, height, blockType=BlockType.NON):
        super().__init__(x, y, width, height)
        self._blockType = blockType

    @property
    def blockType(self):
        return self._blockType
