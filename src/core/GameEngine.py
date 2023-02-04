import pygame

from src.core.PhysicsEngine import PhysicsEngine
from src.plugin.CollisionDetection import CollisionDetection
from src.plugin.GraphicsEngine import GraphicsEngine


class GameEngine:
    clock = pygame.time.Clock()
    player = pygame.Rect(350, 0, 10, 10)

    def __init__(self, generator):
        self.blocks = generator.generate()

        self.physicsEngine = PhysicsEngine(CollisionDetection(self.blocks))
        self.graphicsEngine = GraphicsEngine(self.blocks)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.player, events = self.physicsEngine.movement(self.player)

            if len(events) > 0:
                if events["type"] == "item":
                    self.blocks.remove(events["block"])
                    print("remove Item")

            self.graphicsEngine.draw(self.player)

            self.clock.tick(60)
