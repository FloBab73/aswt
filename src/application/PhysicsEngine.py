from src.application.CollisionDetection import Direction


class PhysicsEngine:
    gravity = 1

    def __init__(self, collision_detection, level):
        self.level = level
        self.collision_detection = collision_detection

    # moves player one pixel at a time to stop at the right moment
    def move(self, subject, objects, distance_x, distance_y):
        x = 0
        y = 0
        if distance_x < 0:
            x = -1
            distance_x = abs(distance_x)
        elif distance_x > 0:
            x = 1
        if distance_y < 0:
            y = -1
            distance_y = abs(distance_y)
        elif distance_y > 0:
            y = 1

        go_x = True
        go_y = True
        while go_x or go_y:
            if distance_x > 0:
                distance_x -= 1
            else:
                x = 0
                go_x = False
            if distance_y > 0:
                distance_y -= 1
            else:
                y = 0
                go_y = False

            subject.move(x, y)

            touch = self.collision_detection.detect(subject, objects, 1)

            if Direction.BOTTOM in touch or Direction.TOP in touch:
                y = 0
            if Direction.LEFT in touch or Direction.RIGHT in touch:
                x = 0

    def move_player(self, key_left, key_up, key_right):

        if self.level.player.stun:
            key_left = False
            key_up = False
            key_right = False
            self.level.player.stun -= 1

        touch = self.collision_detection.detect(self.level.player, self.level.blocks_without_player, 1)

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

        self.move(self.level.player, self.level.blocks_without_player, self.level.player.velocity_x,
                  self.level.player.velocity_y)

    def move_enemies(self):
        for enemy in self.level.enemies:

            touch = self.collision_detection.detect(enemy, self.level.blocks_without_enemies, 1)

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

            self.move(enemy, self.level.blocks_without_enemies, enemy.velocity_x, enemy.velocity_y)