import glob

from src.application.CollisionDetection import CollisionDetection
from src.application.LevelGraphics import LevelGraphics
from src.application.MenuGraphics import MenuGraphics
from src.application.Physics import Physics
from src.domain.Level import Level


class GameManager:
    # inner class for menu
    class Menu:
        def __init__(self, menu_graphics):
            self.len_levels = len(menu_graphics.levels) - 1
            self.menu_graphics = menu_graphics

        def select_next(self):
            if self.menu_graphics.selected == self.len_levels:
                self.menu_graphics.selected = 0
            else:
                self.menu_graphics.selected += 1

        def select_previous(self):
            if self.menu_graphics.selected == 0:
                self.menu_graphics.selected = self.len_levels
            else:
                self.menu_graphics.selected -= 1

        @property
        def selected(self):
            return self.menu_graphics.selected

        def draw_menu(self):
            self.menu_graphics.draw()

        def reset(self):
            self.menu_graphics.selected = 0

    class LevelFiles:
        # expected level path "res/map3.bmp"
        def __init__(self, rootpath):
            if rootpath[-1] != '/':
                rootpath += '/'
            self.levels = glob.glob(rootpath+"*.bmp")
            self.len = len(self.levels)

        def get_level(self, index):
            level = ""
            if self.len > index >= 0:
                level = self.levels[index]
            return level

    def __init__(self, event_handler, game_engine, graphics_engine, generator):
        self.event_handler = event_handler
        self.game_engine = game_engine
        self.graphics_engine = graphics_engine
        self.generator = generator
        self.inMenu = True
        self.levels = self.LevelFiles("res/")
        self.menu = self.Menu(MenuGraphics(self.graphics_engine, self.levels.levels))

        self.level_graphics = LevelGraphics(self.graphics_engine, {})
        self.physics = Physics(CollisionDetection(self.game_engine, self.event_handler), self.levels)

        # Initial event register
        self.event_handler.add(self.event_handler.Events.DRAW, self.draw)
        self.event_handler.add(self.event_handler.Events.KEY_UP, self.menu_up)
        self.event_handler.add(self.event_handler.Events.KEY_DOWN, self.menu_down)
        self.event_handler.add(self.event_handler.Events.KEY_ENTER, self.start_level)
        self.event_handler.add(self.event_handler.Events.DEATH, self.reset_level)
        self.event_handler.add(self.event_handler.Events.QUIT_LEVEL, self.quit_level)

    def init_level(self):
        static_blocks, enemies, player = self.generator.generate(self.levels.get_level(self.menu.selected))
        player.add_event_handler(self.event_handler)
        level = Level(self.event_handler, static_blocks, enemies, player)
        self.level_graphics = LevelGraphics(self.graphics_engine, level)
        self.physics = Physics(CollisionDetection(self.game_engine, self.event_handler), level)

        self.event_handler.add(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
        self.event_handler.add(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)

    # Functions for events
    # Draw Event
    def draw(self):
        if self.inMenu:
            self.menu.draw_menu()
        else:
            self.level_graphics.draw()

    def quit_level(self):
        if not self.inMenu:
            self.menu.reset()
            self.inMenu = True
            self.event_handler.remove(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
            self.event_handler.remove(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)
            self.event_handler.add(self.event_handler.Events.KEY_DOWN, self.menu_down)
            self.event_handler.add(self.event_handler.Events.KEY_UP, self.menu_up)
            self.event_handler.add(self.event_handler.Events.KEY_ENTER, self.start_level)

    # Functions for input events if in menu
    def menu_up(self):
        if self.inMenu:
            self.menu.select_previous()

    def menu_down(self):
        if self.inMenu:
            self.menu.select_next()

    def start_level(self):
        if self.inMenu:
            self.inMenu = False
            self.event_handler.remove(self.event_handler.Events.KEY_DOWN, self.menu_down)
            self.event_handler.remove(self.event_handler.Events.KEY_UP, self.menu_up)
            self.event_handler.add(self.event_handler.Events.QUIT_LEVEL, self.quit_level)
            self.event_handler.add(self.event_handler.Events.RESET, self.reset_level)
            self.init_level()

    def reset_level(self):
        self.event_handler.remove(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
        self.event_handler.remove(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)
        self.init_level()
