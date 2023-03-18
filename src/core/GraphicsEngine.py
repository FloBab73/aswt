from src.core.BlockType import BlockType


class GraphicsEngine:

    def __init__(self, game_engine, game_blocks, active_blocks):
        self.gameEngine = game_engine
        self.game_blocks = game_blocks
        self.activeBlocks = active_blocks
        self.screen = game_engine.init_display(800, 630)
        self.pause = False

    def draw(self):
        if self.pause:
            self.draw_menu()
        else:
            self.draw_level()
            self.draw_hud()
        self.gameEngine.update_display()

    def draw_level(self):
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

    def draw_menu(self):
        self.gameEngine.screen_fill(self.screen, [20, 20, 20])
        self.gameEngine.draw_text(self.screen, "Menu", [390, 100])

    def draw_hud(self):
        self.gameEngine.draw_rect(self.screen, [20, 20, 20], [0, 600, 800, 30])
        self.gameEngine.draw_text(self.screen, "Health: " + str(self.activeBlocks[0].health), [5, 605])
        self.gameEngine.draw_text(self.screen, "Keys: " + str(self.activeBlocks[0].keys), [150, 605])
