from src.core.BlockType import BlockType


class GraphicsEngine:

    def __init__(self, gameEngine, game_blocks, active_blocks):
        self.gameEngine = gameEngine
        self.game_blocks = game_blocks
        self.activeBlocks = active_blocks
        self.screen = gameEngine.init_display(800, 600)

    def draw(self):
        self.gameEngine.screen_fill(self.screen, [200, 150, 0])

        for block in self.game_blocks:
            if block.block_type == BlockType.ITEM_HEAL:
                self.gameEngine.draw_rect(self.screen, (100, 255, 0), block.position())
            elif block.block_type == BlockType.ITEM_KEY:
                self.gameEngine.draw_rect(self.screen, (0, 38, 200), block.position())
            elif block.block_type == BlockType.ITEM_VALUABLE:
                self.gameEngine.draw_rect(self.screen, (0, 200, 200), block.position())
            elif block.block_type == BlockType.DOOR:
                self.gameEngine.draw_rect(self.screen, (64, 64, 64), block.position())
            else:
                self.gameEngine.draw_rect(self.screen, (100, 50, 0), block.position())

        for block in self.activeBlocks:
            if block.block_type == BlockType.PLAYER:
                self.gameEngine.draw_rect(self.screen, (255, 255, 255), block.position())
            elif block.block_type == BlockType.ENEMY:
                self.gameEngine.draw_rect(self.screen, (255, 0, 0), block.position())

        self.gameEngine.update_display()
