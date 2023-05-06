from src.domain.BlockType import BlockType
from src.domain.GraphicsEngine import GraphicsEngine


class GraphicsEngineLevel(GraphicsEngine):

    def __init__(self, game_engine, level):
        super().__init__()
        self.gameEngine = game_engine
        self.screen = game_engine.init_display(self.screen_width, self.screen_height)
        self.level_keys = ""
        self.hud_y = self.screen_height - 30
        self.level = level
        self.level_keys = str(level.keys)
        self.blockColors = {
                        BlockType.ITEM_HEAL: (100, 255, 0),
                        BlockType.ITEM_KEY: (0, 38, 200),
                        BlockType.ITEM_VALUABLE: (0, 200, 200),
                        BlockType.DOOR: (64, 64, 64),
                        BlockType.PLAYER: (255, 255, 255),
                        BlockType.ENEMY: (255, 0, 0),
                        BlockType.WALL: (100, 50, 0),
        }

    def draw(self):
        self.draw_level()
        self.draw_hud()
        self.gameEngine.update_display()

    def draw_level(self):
        self.gameEngine.screen_fill(self.screen, [200, 150, 0])
        for block in self.level.all_blocks:
            if block.block_type in self.blockColors:
                self.gameEngine.draw_rect(self.screen, self.blockColors[block.block_type], block.position())

    def draw_hud(self):
        self.gameEngine.draw_rect(self.screen, [20, 20, 20], [0, self.hud_y, self.screen_width, 30])
        self.gameEngine.draw_text(self.screen, "Health: " + self.level.player.health_str, [5, 605])
        self.gameEngine.draw_text(self.screen, "Keys: " + self.level.player.keys_str + " / " + self.level_keys,
                                  [150, 605])
