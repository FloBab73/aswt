from src.core.BlockType import BlockType
from src.core.Player import Player
from src.plugin.PygameGameBlock import PygameGameBlock


class PygamePlayer(Player, PygameGameBlock):
    def __init__(self, physics_engine, game_blocks, x=0, y=0, width=10, height=10):
        Player.__init__(self, physics_engine, game_blocks, x, y, width, height)
        PygameGameBlock.__init__(self, x, y, width, height, BlockType.PLAYER)

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
