from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class Player:

    def __init__(self, x, y, w, h):
        self.pos = GameBlock(x, y, w, h, BlockType.PLAYER)

    def position(self):
        return [self.pos.x, self.pos.y, self.pos.width, self.pos.height]
