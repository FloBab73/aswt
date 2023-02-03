import pygame
from src.core.BlockType import BlockType


class GraphicsEngine:

    def __init__(self, blocks):
        self.screen = pygame.display.set_mode((800, 600))
        self.blocks = blocks

    def draw(self, player):
        self.screen.fill(0)

        for block in self.blocks:
            if block.blockType == BlockType.ITEM:
                pygame.draw.rect(self.screen, (128, 0, 0), block)
            else:
                pygame.draw.rect(self.screen, (0, 255, 0), block)

        pygame.draw.rect(self.screen, (255, 255, 255), player)

        pygame.display.update()
