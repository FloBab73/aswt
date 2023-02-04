import pygame

from src.core.BlockType import BlockType
from src.core.GraphicsEngine import GraphicsEngine


class PygameGraphics(GraphicsEngine):
    screen = None

    def __init__(self, gameBlocks, activeBlocks):
        super().__init__(gameBlocks, activeBlocks)
        self.screen = pygame.display.set_mode((800, 600))

    def draw(self):
        self.screen.fill(0)

        for gameBlock in self.gameBlocks:
            if gameBlock.blockType == BlockType.ITEM_HEAL:
                pygame.draw.rect(self.screen, (255, 255, 0), gameBlock.pygameBlock)
            else:
                pygame.draw.rect(self.screen, (0, 255, 0), gameBlock.pygameBlock)

        for activeBlock in self.activeBlocks:
            if activeBlock.blockType == BlockType.PLAYER:
                pygame.draw.rect(self.screen, (255, 255, 255), activeBlock.pygameBlock)

        pygame.display.update()
