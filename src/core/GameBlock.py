from src.core.BlockType import BlockType


class GameBlock:
    def __init__(self, x, y, width, height, blockType=BlockType.NON):
        self.blockType = blockType
        self.height = height
        self.width = width
        self.y = y
        self.x = x
