from src.domain.BlockType import BlockType


class GraphicsEngineLevel:

    def __init__(self, game_engine, level):
        self.screen_width = 800
        self.screen_height = 630
        self.gameEngine = game_engine
        self.screen = game_engine.init_display(self.screen_width, self.screen_height)
        self.level_keys = ""
        self.hud_y = self.screen_height-30
        self.level = level
        self.level_keys = str(level.keys)

    def draw_level(self):
        self.gameEngine.screen_fill(self.screen, [200, 150, 0])

        for block in self.level.all_blocks:
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

        self.draw_hud()
        self.gameEngine.update_display()

    def draw_hud(self):
        self.gameEngine.draw_rect(self.screen, [20, 20, 20], [0, self.hud_y, self.screen_width, 30])
        self.gameEngine.draw_text(self.screen, "Health: " + self.level.player.health_str, [5, 605])
        self.gameEngine.draw_text(self.screen, "Keys: "+self.level.player.keys_str+" / "+self.level_keys, [150, 605])
