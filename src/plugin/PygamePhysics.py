import pygame

from src.core.PhysicsEngine import PhysicsEngine
from src.core.Player import Player


class PygamePhysics(PhysicsEngine):
    velocity_x = 0
    velocity_y = 0
    gravity = 1
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, collisionDetection):
        super().__init__(collisionDetection)

    # moves player one pixel at a time to stop at the right moment
    def move(self, player, distance_x, distance_y):
        x = 0
        y = 0
        event = []
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
            touch = self.collisionDetection.detect(player, 1)

            if touch["hasEvent"]:
                event = touch["event"]
            if touch["bottom"] or touch["top"]:
                y = 0
            if touch["left"] or touch["right"]:
                x = 0

        return player, event

    # checks for button input and calculates movement
    def movement(self, player):
        pygamePlayer = pygame.Rect(player.position())

        touch = self.collisionDetection.detect(pygamePlayer, 1)
        key = pygame.key.get_pressed()

        if touch["bottom"]:
            self.velocity_y = 0
        elif touch["top"]:
            self.velocity_y = self.gravity
        else:
            self.velocity_y += self.gravity

        if touch["left"]:
            if self.velocity_x < 0:
                self.velocity_x = 0
        else:
            if key[pygame.K_LEFT]:
                if self.velocity_x >= -self.maxSpeed:
                    self.velocity_x -= self.acceleration
            else:
                if self.velocity_x < 0:
                    self.velocity_x += self.deceleration

        if touch["right"]:
            if self.velocity_x > 0:
                self.velocity_x = 0
        else:
            if key[pygame.K_RIGHT]:
                if self.velocity_x <= self.maxSpeed:
                    self.velocity_x += self.acceleration
            else:
                if self.velocity_x > 0:
                    self.velocity_x -= self.deceleration

        if key[pygame.K_UP] and touch["bottom"]:
            self.velocity_y = -9

        pygamePlayer, event = self.move(pygamePlayer, self.velocity_x, self.velocity_y)
        player = Player(pygamePlayer.x, pygamePlayer.y, pygamePlayer.width, pygamePlayer.height)
        return player, event
