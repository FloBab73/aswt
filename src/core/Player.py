from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class Player(GameBlock):
    velocity_x = 0
    velocity_y = 0
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, physicsEngine, gameBlocks, x=0, y=0, width=10, height=10):
        self.gameBlocks = gameBlocks
        self.physicsEngine = physicsEngine
        self.x = x
        self.y = y
        super().__init__(x, y, width, height, BlockType.PLAYER)

    def movement(self, key):
        pass
