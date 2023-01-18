import pygame


class GraphicsEngine:

    def __init__(self, blocks):
        self.screen = pygame.display.set_mode((800, 600))
        self.blocks = blocks

    def draw(self, player):
        self.screen.fill(0)

        for block in self.blocks:
            pygame.draw.rect(self.screen, (0, 255, 0), block)

        pygame.draw.rect(self.screen, (255, 255, 255), player)

        pygame.display.update()
