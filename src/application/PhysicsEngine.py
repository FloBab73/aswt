from src.application.BlockMover import BlockMover
from src.application.CollisionDetection import Direction


class PhysicsEngine:
    gravity = 1

    def __init__(self, collision_detection, level):
        self.level = level
        self.collision_detection = collision_detection
        self.block_mover = BlockMover(collision_detection)

    def move_player(self, key_left, key_up, key_right):

        if self.level.player.stun:
            key_left = False
            key_up = False
            key_right = False
            self.level.player.stun -= 1

        touch = self.collision_detection.detect(self.level.player, self.level.blocks_without_player, 1, 1)

        if Direction.BOTTOM in touch:
            if self.level.player.velocity_y > 0:
                self.level.player.velocity_y = 0
        elif Direction.TOP in touch:
            self.level.player.velocity_y = self.gravity
        else:
            self.level.player.velocity_y += self.gravity

        if Direction.LEFT in touch:
            if self.level.player.velocity_x < 0:
                self.level.player.velocity_x = 0
        else:
            if key_left:
                if self.level.player.velocity_x >= -self.level.player.max_speed:
                    self.level.player.velocity_x -= self.level.player.acceleration
            else:
                if self.level.player.velocity_x < 0:
                    self.level.player.velocity_x += self.level.player.deceleration

        if Direction.RIGHT in touch:
            if self.level.player.velocity_x > 0:
                self.level.player.velocity_x = 0
        else:
            if key_right:
                if self.level.player.velocity_x <= self.level.player.max_speed:
                    self.level.player.velocity_x += self.level.player.acceleration
            else:
                if self.level.player.velocity_x > 0:
                    self.level.player.velocity_x -= self.level.player.deceleration

        if key_up and Direction.BOTTOM in touch:
            self.level.player.velocity_y = -9

        self.block_mover.move_block(self.level.player, self.level.blocks_without_player, self.level.player.velocity_x,
                                    self.level.player.velocity_y)

    def move_enemies(self):
        for enemy in self.level.enemies:

            touch = self.collision_detection.detect(enemy, self.level.blocks_without_enemies, 1, 1)

            if Direction.BOTTOM in touch:
                enemy.velocity_y = 0
            elif Direction.TOP in touch:
                enemy.velocity_y = self.gravity
            else:
                enemy.velocity_y += self.gravity
            if Direction.RIGHT in touch and Direction.LEFT in touch:
                enemy.velocity_x = 0
            elif Direction.LEFT in touch:
                enemy.velocity_x = enemy.acceleration
            elif Direction.RIGHT in touch:
                enemy.velocity_x = -enemy.acceleration
            else:
                if 0 > enemy.velocity_x > -enemy.max_speed:
                    enemy.velocity_x -= enemy.acceleration
                elif 0 <= enemy.velocity_x < enemy.max_speed:
                    enemy.velocity_x += enemy.acceleration

            self.block_mover.move_block(enemy, self.level.blocks_without_enemies, enemy.velocity_x, enemy.velocity_y)
