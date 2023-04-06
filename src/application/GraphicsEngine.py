from src.domain.BlockType import BlockType


class GraphicsEngine:

    def __init__(self, game_engine, level):
        self.screen_width = 800
        self.screen_height = 630
        self.gameEngine = game_engine
        self.level = level
        self.screen = game_engine.init_display(self.screen_width, self.screen_height)
        self.level_keys = str(level.keys)
        self.hud_y = self.screen_height-30

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

    def draw_menu(self, levels, selected):
        center_x = self.screen_width/2
        box_width = 300
        box_height = 75
        box_pos_y = 150
        box_pos_x = center_x - box_width/2
        self.gameEngine.screen_fill(self.screen, [20, 20, 20])
        self.gameEngine.draw_text(self.screen, "Select", [center_x - 30, 100])
        i = 1
        for level in levels:
            self.gameEngine.draw_button(
                self.screen,
                (100, 200, 100) if i-1 == selected else (100, 100, 100),
                [box_pos_x, box_pos_y, box_width, box_height],
                "Level " + str(i) + " " + level
            )
            box_pos_y += box_height + 10
            i += 1

        self.gameEngine.update_display()