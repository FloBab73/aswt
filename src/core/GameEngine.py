import pygame

from src.core.Player import Player


class GameEngine:
    clock = pygame.time.Clock()
    player = Player(350, 0, 10, 10)

    def __init__(self, gameBlocks, graphicsEngine, physicsEngine):
        self.graphicsEngine = graphicsEngine
        self.gameBlocks = gameBlocks
        self.physicsEngine = physicsEngine

        self.graphicsEngine.init(self.gameBlocks)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.player, events = self.physicsEngine.movement(self.player)

            if len(events) > 0:
                if events["type"] == "item":
                    self.gameBlocks.remove(events["block"])

            self.graphicsEngine.draw(self.player)

            self.clock.tick(60)
