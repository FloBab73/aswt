import pygame

from CollisionDetection import CollisionDetection


class PhysicsEngine:
    velocityX = 0
    velocityY = 0
    gravity = 1
    acceleration = 1
    deceleration = 1

    def __init__(self, blocks):
        self.cD = CollisionDetection(blocks)

    def move(self, player, distance_x, distance_y):
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

            player = player.move(x, y)
            touch = self.cD.detect(player, 1)

            if touch["bottom"]:
                y = 0
            if touch["top"]:
                y = 0
            if touch["left"] or touch["right"]:
                x = 0
        return player

    def movement(self, player):
        touch = self.cD.detect(player, 1)
        if touch["top"]:
            self.velocityY = 0
        if touch["bottom"]:
            self.velocityY = 0
        else:
            self.velocityY = self.velocityY + self.gravity

        key = pygame.key.get_pressed()
        if not touch["left"]:
            if key[pygame.K_LEFT]:
                if self.velocityX >= -2:
                    self.velocityX -= self.acceleration
            else:
                if self.velocityX < 0:
                    self.velocityX += self.deceleration
        else:
            if self.velocityX < 0:
                self.velocityX = 0

        if not touch["right"]:
            if key[pygame.K_RIGHT]:
                if self.velocityX <= 2:
                    self.velocityX += self.acceleration
            else:
                if self.velocityX > 0:
                    self.velocityX -= self.deceleration
        else:
            if self.velocityX > 0:
                self.velocityX = 0

        if key[pygame.K_SPACE] and touch["bottom"]:
            self.velocityY = -9

        player = self.move(player, self.velocityX, self.velocityY)

        return player
