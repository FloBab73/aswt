from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.core.CollisionDetection import CollisionDetection
from src.core.GameBlock import GameBlock
from src.core.PhysicsEngine import PhysicsEngine
from src.core.Player import Player
from src.plugin.EventHandler import EventHandler


class TestPlayer(TestCase):

    def test_gravity_and_stop(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()

        objects = [GameBlock(0, 17, 20, 20)]
        player = Player(PhysicsEngine(CollisionDetection(game_engine, event_handler)), objects)
        key = {
            "up": False,
            "right": False,
            "bottom": False,
            "left": False,
        }

        player.movement(key)
        assert player.y == 1
        player.movement(key)
        assert player.y == 3
        player.movement(key)
        assert player.y == 6
        player.movement(key)
        assert player.y == 7

    def test_jump(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()

        objects = [GameBlock(0, 30, 20, 20), GameBlock(0, -5, 20, 5)]
        player = Player(PhysicsEngine(CollisionDetection(game_engine, event_handler)), objects, 0, 20)
        key_empty = {
            "up": False,
            "right": False,
            "left": False,
            "bottom": False,
        }

        key_jump = {
            "up": True,
            "right": False,
            "left": False,
            "bottom": False,
        }

        player.movement(key_jump)
        assert player.y == 11
        player.movement(key_empty)
        assert player.y == 3
        player.movement(key_empty)
        assert player.y == 0
