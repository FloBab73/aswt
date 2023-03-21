from src.domain.GameBlock import GameBlock


class MovingGameBlock(GameBlock):
    acceleration = 1
    deceleration = 1
    maxSpeed = 2
    velocity_x = 0
    velocity_y = 0

    def __init__(self, x, y, width, height, block_type):
        super().__init__(x, y, width, height, block_type)

    def move(self, x, y):
        self.x += x
        self.y += y
