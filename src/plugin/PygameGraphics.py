import pygame

from src.core.BlockType import BlockType
from src.core.GraphicsEngine import GraphicsEngine


class PygameGraphics(GraphicsEngine):
    screen = None

    def __init__(self, game_blocks, active_blocks):
        super().__init__(game_blocks, active_blocks)
        self.screen = pygame.display.set_mode((800, 600))

    def draw(self):
        self.screen.fill([200, 150, 0])

        for block in self.game_blocks:
            if block.block_type == BlockType.ITEM_HEAL:
                pygame.draw.rect(self.screen, (100, 255, 0), block.position())
            elif block.block_type == BlockType.ITEM_KEY:
                pygame.draw.rect(self.screen, (0, 38, 200), block.position())
            elif block.block_type == BlockType.ITEM_VALUABLE:
                pygame.draw.rect(self.screen, (0, 200, 200), block.position())
            elif block.block_type == BlockType.DOOR:
                pygame.draw.rect(self.screen, (64, 64, 64), block.position())
            else:
                pygame.draw.rect(self.screen, (100, 50, 0), block.position())

        for block in self.activeBlocks:
            if block.block_type == BlockType.PLAYER:
                pygame.draw.rect(self.screen, (255, 255, 255), block.position())
            elif block.block_type == BlockType.ENEMY:
                pygame.draw.rect(self.screen, (255, 0, 0), block.position())

        pygame.display.update()
