import sys

import pygame

from src.core.PhysicsEngine import PhysicsEngine
from src.plugin.GraphicsEngine import GraphicsEngine


class GameEngine:
    clock = pygame.time.Clock()
    player = pygame.Rect(350, 0, 10, 10)

    def __init__(self, generator):
        self.generator = generator
        self.blocks = generator.generate()

        self.pEngine = PhysicsEngine(self.blocks)
        self.gEngine = GraphicsEngine(self.blocks)

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            player = self.pEngine.movement(self.player)
            self.gEngine.draw(player)

            self.clock.tick(60)
