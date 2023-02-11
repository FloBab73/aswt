import pygame

from src.core.BlockType import BlockType
from src.core.GraphicsEngine import GraphicsEngine


class PygameGraphics(GraphicsEngine):
    screen = None

    def __init__(self, gameBlocks, activeBlocks):
        super().__init__(gameBlocks, activeBlocks)
        self.screen = pygame.display.set_mode((800, 600))

    def draw(self):
        self.screen.fill([200, 150, 0])

        for gameBlock in self.gameBlocks:
            if gameBlock.blockType == BlockType.ITEM_HEAL:
                pygame.draw.rect(self.screen, (100, 255, 0), gameBlock.position())
            elif gameBlock.blockType == BlockType.ITEM_KEY:
                pygame.draw.rect(self.screen, (0, 38, 200), gameBlock.position())
            elif gameBlock.blockType == BlockType.ITEM_VALUABLE:
                pygame.draw.rect(self.screen, (0, 200, 200), gameBlock.position())
            elif gameBlock.blockType == BlockType.DOOR:
                pygame.draw.rect(self.screen, (64, 64, 64), gameBlock.position())
            else:
                pygame.draw.rect(self.screen, (100, 50, 0), gameBlock.position())

        for activeBlock in self.activeBlocks:
            if activeBlock.blockType == BlockType.PLAYER:
                pygame.draw.rect(self.screen, (255, 255, 255), activeBlock.position())
            if activeBlock.blockType == BlockType.ENEMY:
                pygame.draw.rect(self.screen, (255, 0, 0), activeBlock.position())

        pygame.display.update()
