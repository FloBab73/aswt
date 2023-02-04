import pygame

from src.core.BlockType import BlockType
from src.core.GraphicsEngine import GraphicsEngine


class PygameGraphics(GraphicsEngine):
    screen = None

    def init(self, blocks):
        super().init(blocks)
        self.screen = pygame.display.set_mode((800, 600))

    def draw(self, player):
        pygamePlayer = pygame.Rect(player.position())
        self.screen.fill(0)

        for block in self.blocks:
            if block.blockType == BlockType.ITEM:
                pygame.draw.rect(self.screen, (128, 0, 0), block.pygameBlock)
            else:
                pygame.draw.rect(self.screen, (0, 255, 0), block.pygameBlock)

        pygame.draw.rect(self.screen, (255, 255, 255), pygamePlayer)

        pygame.display.update()
