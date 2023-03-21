from src.domain.BlockType import BlockType


class GraphicsEngine:

    def __init__(self, game_engine, level):
        self.gameEngine = game_engine
        self.level = level
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
        all_blocks = self.level.static_blocks + self.level.enemies + [self.level.player]

        for block in all_blocks:
            match block.block_type:
                case BlockType.ITEM_HEAL:
                    self.gameEngine.draw_rect(self.screen, (100, 255, 0), block.position())
                case BlockType.ITEM_KEY:
                    self.gameEngine.draw_rect(self.screen, (0, 38, 200), block.position())
                case BlockType.ITEM_VALUABLE:
                    self.gameEngine.draw_rect(self.screen, (0, 200, 200), block.position())
                case BlockType.DOOR:
                    self.gameEngine.draw_rect(self.screen, (64, 64, 64), block.position())
                case BlockType.PLAYER:
                    self.gameEngine.draw_rect(self.screen, (255, 255, 255), block.position())
                case BlockType.ENEMY:
                    self.gameEngine.draw_rect(self.screen, (255, 0, 0), block.position())
                case BlockType.WALL:
                    self.gameEngine.draw_rect(self.screen, (100, 50, 0), block.position())

    def draw_menu(self):
        self.gameEngine.screen_fill(self.screen, [20, 20, 20])
        self.gameEngine.draw_text(self.screen, "Menu", [390, 100])

    def draw_hud(self):
        self.gameEngine.draw_rect(self.screen, [20, 20, 20], [0, 600, 800, 30])
        self.gameEngine.draw_text(self.screen, "Health: " + str(self.level.player.health), [5, 605])
        self.gameEngine.draw_text(self.screen, "Keys: " + str(self.level.player.keys), [150, 605])
