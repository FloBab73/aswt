from src.domain.ActiveGameBlock import ActiveGameBlock
from src.domain.BlockType import BlockType


class Enemy(ActiveGameBlock):

    def __init__(self, x=0, y=0, width=10, height=10, max_speed=1):
        super().__init__(x, y, width, height, BlockType.ENEMY)
        self.max_speed = max_speed
        self.x = x
        self._startX = x
        self.y = y
        self._startY = y

    def resetPos(self):
        self.x = self._startX
        self.y = self._startY
