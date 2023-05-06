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

    def draw(self):
        self.draw_level()
        self.draw_hud()
        self.gameEngine.update_display()

    def draw_level(self):
        self.gameEngine.screen_fill(self.screen, [200, 150, 0])
        for block in self.level.all_blocks:
            self.gameEngine.draw_rect(self.screen, block.color, block.position())

    def draw_hud(self):
        self.gameEngine.draw_rect(self.screen, [20, 20, 20], [0, self.hud_y, self.screen_width, 30])
        self.gameEngine.draw_text(self.screen, "Health: " + self.level.player.health_str, [5, 605])
        self.gameEngine.draw_text(self.screen, "Keys: " + self.level.player.keys_str + " / " + self.level_keys,
                                  [150, 605])
