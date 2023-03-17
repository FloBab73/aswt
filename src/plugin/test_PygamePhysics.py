from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.core.CollisionDetection import CollisionDetection
from src.core.GameBlock import GameBlock
from src.core.PhysicsEngine import PhysicsEngine
from src.plugin.EventHandler import EventHandler


class TestPhysics(TestCase):
    def test_move_right_against_wall(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()
        subject = GameBlock(10, 10, 20, 20)
        objects = [GameBlock(35, 10, 20, 20)]

        physics = PhysicsEngine(CollisionDetection(game_engine, event_handler))

        physics.move(subject, objects, 1, 0)
        assert subject.x == 11
        physics.move(subject, objects, 10, 0)
        assert subject.x == 15
