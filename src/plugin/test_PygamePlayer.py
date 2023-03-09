from unittest import TestCase

from src.plugin.EventHandler import EventHandler
from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock
from src.plugin.PygamePhysics import PygamePhysics
from src.plugin.PygamePlayer import PygamePlayer


class TestPygamePlayer(TestCase):

    def test_gravity_and_stop(self):
        event_handler = EventHandler()
        objects = [PygameGameBlock(0, 17, 20, 20)]
        player = PygamePlayer(PygamePhysics(PygameCollisionDetection(event_handler)), objects)
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
        objects = [PygameGameBlock(0, 30, 20, 20), PygameGameBlock(0, -5, 20, 5)]
        player = PygamePlayer(PygamePhysics(PygameCollisionDetection(event_handler)), objects, 0, 20)
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
