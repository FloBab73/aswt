from src.domain.BlockType import BlockType
from src.domain.MovingGameBlock import MovingGameBlock


class Enemy(MovingGameBlock):

    def __init__(self, x=0, y=0, width=10, height=10):
        super().__init__(x, y, width, height, BlockType.ENEMY)
        self.x = x
        self._startX = x
        self.y = y
        self._startY = y

    def death(self):
        print("Enemy killed")

    def resetPos(self):
        self.x = self._startX
        self.y = self._startY
