from src.domain.BlockType import BlockType


class GameBlock:
    def __init__(self, x, y, width, height, color=(0, 0, 0), block_type=BlockType.NONE):
        self.block_type = block_type
        self.height = height
        self.width = width
        self.color = color
        self.y = y
        self.x = x

    def position(self):
        return [self.x, self.y, self.width, self.height]
