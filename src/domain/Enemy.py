from src.domain.ActiveGameBlock import ActiveGameBlock
from src.domain.BlockType import BlockType


class Enemy(ActiveGameBlock):

    def __init__(self, x=0, y=0, width=10, height=10, max_speed=1):
        super().__init__(x, y, width, height, BlockType.ENEMY)
        self.max_speed = max_speed
