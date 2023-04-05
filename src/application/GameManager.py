from src.application.CollisionDetection import CollisionDetection
from src.application.GraphicsEngine import GraphicsEngine
from src.adapter.BlocksGenerator import BlocksGenerator
from src.application.PhysicsEngine import PhysicsEngine
from src.domain.Level import Level
import glob


class GameManager:
    # inner class for menu
    class Menu:
        def __init__(self, number_of_levels):
            self.selected = 0
            self.nr_of_levels = number_of_levels-1

        def select_next(self):
            if self.selected == self.nr_of_levels:
                self.selected = 0
            else:
                self.selected += 1

        def select_previous(self):
            if self.selected == 0:
                self.selected = self.nr_of_levels
            else:
                self.selected -= 1

        def reset(self):
            self.selected = 0

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

    def __init__(self, event_handler, game_engine):
        self.event_handler = event_handler
        self.game_engine = game_engine
        self.inMenu = True
        self.levels = self.LevelFiles("res/")
        self.menu = self.Menu(self.levels.len)

        self.graphics_engine = GraphicsEngine(self.game_engine, {})
        self.physics = PhysicsEngine(CollisionDetection(self.game_engine, self.event_handler), self.levels)

        # Initial event register
        self.event_handler.add(event_handler.Events.DRAW, self.draw)
        self.event_handler.add(self.event_handler.Events.KEY_UP, self.menu_up)
        self.event_handler.add(self.event_handler.Events.KEY_DOWN, self.menu_down)
        self.event_handler.add(self.event_handler.Events.KEY_ENTER, self.start_level)
        self.event_handler.add(self.event_handler.Events.DEATH, self.quit_level)
        self.event_handler.add(self.event_handler.Events.KEY_ESC, self.quit_level)

    def init_level(self):
        static_blocks, enemies, player = BlocksGenerator().generate(self.levels.get_level(self.menu.selected))
        player.add_event_handler(self.event_handler)
        level = Level(self.event_handler, static_blocks, enemies, player)
        self.graphics_engine = GraphicsEngine(self.game_engine, level)
        self.physics = PhysicsEngine(CollisionDetection(self.game_engine, self.event_handler), level)

        self.event_handler.add(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
        self.event_handler.add(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)

    # Functions for events
    # Draw Event
    def draw(self):
        if self.inMenu:
            self.graphics_engine.draw_menu(self.levels.levels, self.menu.selected)
        else:
            self.graphics_engine.draw_level()

    def quit_level(self):
        if not self.inMenu:
            self.menu.reset()
            self.inMenu = True
            self.event_handler.add(self.event_handler.Events.KEY_DOWN, self.menu_down)
            self.event_handler.add(self.event_handler.Events.KEY_UP, self.menu_up)
            self.event_handler.add(self.event_handler.Events.KEY_ENTER, self.start_level)
            self.event_handler.remove(self.event_handler.Events.MOVE_PLAYER, self.physics.move_player)
            self.event_handler.remove(self.event_handler.Events.MOVE_ENEMIES, self.physics.move_enemies)

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
            self.event_handler.add(self.event_handler.Events.QUIT, self.quit_level)
            self.init_level()
