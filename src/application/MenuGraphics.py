from src.domain.Graphics import Graphics


class MenuGraphics(Graphics):

    def __init__(self, graphics_engine, levels):
        super().__init__()
        self.graphics_engine = graphics_engine
        self.screen = graphics_engine.init_display(self.screen_width, self.screen_height)
        self.selected = 0
        self.levels = levels

    def draw(self):
        center_x = self.screen_width / 2
        box_width = 300
        box_height = 75
        box_pos_y = 150
        box_pos_x = center_x - box_width / 2
        self.graphics_engine.screen_fill(self.screen, [20, 20, 20])
        self.graphics_engine.draw_text(self.screen, "Select", [center_x - 30, 100])
        i = 1
        for level in self.levels:
            self.graphics_engine.draw_button(
                self.screen,
                (100, 200, 100) if i - 1 == self.selected else (100, 100, 100),
                [box_pos_x, box_pos_y, box_width, box_height],
                "Level " + str(i) + " " + level
            )
            box_pos_y += box_height + 10
            i += 1

        self.graphics_engine.update_display()
