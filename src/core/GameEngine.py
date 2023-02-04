import pygame


class GameEngine:
    clock = pygame.time.Clock()

    def __init__(self, gameBlocks, graphicsEngine, physicsEngine):
        self.graphicsEngine = graphicsEngine
        self.gameBlocks = gameBlocks
        self.physicsEngine = physicsEngine

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            events = self.physicsEngine.movement()

            if len(events) > 0:
                if events["type"] == "item":
                    self.gameBlocks.remove(events["block"])

            self.graphicsEngine.draw()

            self.clock.tick(60)
