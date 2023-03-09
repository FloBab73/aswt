from src.core.BlockType import BlockType


class GameBlock:
    def __init__(self, x, y, width, height, block_type=BlockType.NONE):
        self.block_type = block_type
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def position(self):
        return [self.x, self.y, self.width, self.height]
