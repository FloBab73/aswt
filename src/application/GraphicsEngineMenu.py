from src.domain.GraphicsEngine import GraphicsEngine
from src.domain.BlockType import BlockType


class GraphicsEngineMenu(GraphicsEngine):

    def __init__(self, game_engine, levels):
        self.screen_width = 800
        self.screen_height = 630
        self.gameEngine = game_engine
        self.screen = game_engine.init_display(self.screen_width, self.screen_height)
        self.selected = 0
        self.levels = levels

    def draw(self):
        center_x = self.screen_width/2
        box_width = 300
        box_height = 75
        box_pos_y = 150
        box_pos_x = center_x - box_width/2
        self.gameEngine.screen_fill(self.screen, [20, 20, 20])
        self.gameEngine.draw_text(self.screen, "Select", [center_x - 30, 100])
        i = 1
        for level in self.levels:
            self.gameEngine.draw_button(
                self.screen,
                (100, 200, 100) if i-1 == self.selected else (100, 100, 100),
                [box_pos_x, box_pos_y, box_width, box_height],
                "Level " + str(i) + " " + level
            )
            box_pos_y += box_height + 10
            i += 1

        self.gameEngine.update_display()
