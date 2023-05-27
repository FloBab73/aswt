from src.domain.Graphics import Graphics


class LevelGraphics(Graphics):

    def __init__(self, graphics_engine, level):
        super().__init__()
        self.graphics_engine = graphics_engine
        self.screen = self.graphics_engine.init_display(self.screen_width, self.screen_height)
        self.level_keys = ""
        self.hud_y = self.screen_height - 30
        self.level = level
        self.level_keys = str(level.keys)

    def draw(self):
        self.draw_level()
        self.draw_hud()
        self.graphics_engine.update_display()

    def draw_level(self):
        self.graphics_engine.screen_fill(self.screen, [200, 150, 0])
        for block in self.level.all_blocks:
            self.graphics_engine.draw_rect(self.screen, block.color, block.position())

    def draw_hud(self):
        self.graphics_engine.draw_rect(self.screen, [20, 20, 20], [0, self.hud_y, self.screen_width, 30])
        self.graphics_engine.draw_text(self.screen, "Health: " + self.level.player.health_str, [5, 605])
        self.graphics_engine.draw_text(self.screen, "Keys: " + self.level.player.keys_str + " / " + self.level_keys,
                                       [150, 605])
