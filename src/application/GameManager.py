import glob

from src.application.CollisionDetection import CollisionDetection
from src.application.GraphicsEngineLevel import GraphicsEngineLevel
from src.application.GraphicsEngineMenu import GraphicsEngineMenu
from src.application.PhysicsEngine import PhysicsEngine
from src.domain.Level import Level


class GameManager:
    # inner class for menu
    class Menu:
        def __init__(self, graphics_engine_menu):
            self.len_levels = len(graphics_engine_menu.levels) - 1
            self.graphics_engine_menu = graphics_engine_menu

        def select_next(self):
            if self.graphics_engine_menu.selected == self.len_levels:
                self.graphics_engine_menu.selected = 0
            else:
                self.graphics_engine_menu.selected += 1

        def select_previous(self):
            if self.graphics_engine_menu.selected == 0:
                self.graphics_engine_menu.selected = self.len_levels
            else:
                self.graphics_engine_menu.selected -= 1

        @property
        def selected(self):
            return self.graphics_engine_menu.selected

        def draw_menu(self):
            self.graphics_engine_menu.draw()

        def reset(self):
            self.graphics_engine_menu.selected = 0

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

    def __init__(self, event_handler, game_engine, generator):
        self.event_handler = event_handler
        self.game_engine = game_engine
        self.generator = generator
        self.inMenu = True
        self.levels = self.LevelFiles("res/")
        self.menu = self.Menu(GraphicsEngineMenu(game_engine, self.levels.levels))

        self.graphics_engine = GraphicsEngineLevel(self.game_engine, {})
        self.physics = PhysicsEngine(CollisionDetection(self.game_engine, self.event_handler), self.levels)

        # Initial event register
        self.event_handler.add(event_handler.Events.DRAW, self.draw)
        self.event_handler.add(self.event_handler.Events.KEY_UP, self.menu_up)
        self.event_handler.add(self.event_handler.Events.KEY_DOWN, self.menu_down)
        self.event_handler.add(self.event_handler.Events.KEY_ENTER, self.start_level)
        self.event_handler.add(self.event_handler.Events.DEATH, self.reset_level)
        self.event_handler.add(self.event_handler.Events.QUIT_LEVEL, self.quit_level)

    def init_level(self):
        static_blocks, enemies, player = self.generator.generate(self.levels.get_level(self.menu.selected))
        player.add_event_handler(self.event_handler)
        level = Level(self.event_handler, static_blocks, enemies, player)
        self.graphics_engine = GraphicsEngineLevel(self.game_engine, level)
        self.physics = PhysicsEngine(CollisionDetection(self.game_engine, self.event_handler), level)

        self.event_handler.add(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
        self.event_handler.add(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)

    # Functions for events
    # Draw Event
    def draw(self):
        if self.inMenu:
            self.menu.draw_menu()
        else:
            self.graphics_engine.draw()

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
