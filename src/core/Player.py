from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class Player(GameBlock):
    velocity_x = 0
    velocity_y = 0
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, physics_engine, game_blocks, x=0, y=0, width=10, height=10):
        super().__init__(x, y, width, height, BlockType.PLAYER)
        self.game_blocks = game_blocks
        self.physics_engine = physics_engine
        self.x = x
        self._startX = x
        self.y = y
        self._startY = y
        self._health = 100

    def movement(self, key):

        touch = self.physics_engine.collision_detection.detect(self, self.game_blocks, 1)

        if touch["bottom"]:
            self.velocity_y = 0
        elif touch["top"]:
            self.velocity_y = self.physics_engine.gravity
        else:
            self.velocity_y += self.physics_engine.gravity

        if touch["left"]:
            if self.velocity_x < 0:
                self.velocity_x = 0
        else:
            if key["left"]:
                if self.velocity_x >= -self.maxSpeed:
                    self.velocity_x -= self.acceleration
            else:
                if self.velocity_x < 0:
                    self.velocity_x += self.deceleration

        if touch["right"]:
            if self.velocity_x > 0:
                self.velocity_x = 0
        else:
            if key["right"]:
                if self.velocity_x <= self.maxSpeed:
                    self.velocity_x += self.acceleration
            else:
                if self.velocity_x > 0:
                    self.velocity_x -= self.deceleration

        if key["up"] and touch["bottom"]:
            self.velocity_y = -9

        self.physics_engine.move(self, self.game_blocks, self.velocity_x, self.velocity_y)

    def modify_health(self, modifier):
        self._health += modifier
        print("Player Health: ", self._health)
        if self._health <= 0:
            self.death()

    def death(self):
        print("X.X Du bist Tot X.X")

    def resetPos(self):
        self.x = self._startX
        self.y = self._startY
        self._health = 100