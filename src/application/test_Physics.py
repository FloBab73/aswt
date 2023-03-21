from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection
from src.application.PhysicsEngine import PhysicsEngine
from src.domain.GameBlock import GameBlock
from src.plugin.EventHandler import EventHandler


def initialise_physics():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return PhysicsEngine(CollisionDetection(game_engine, event_handler))


class TestPhysics(TestCase):

    def test_move_right(self):
        physics = initialise_physics()
        subject = GameBlock(10, 10, 20, 20)
        objects = [GameBlock(35, 10, 20, 20)]

        physics.move(subject, objects, 1, 0)
        assert subject.x == 11

    def test_move_against_wall(self):
        physics = initialise_physics()
        subject = GameBlock(10, 10, 20, 20)
        objects = [GameBlock(35, 10, 20, 20)]

        physics.move(subject, objects, 10, 0)
        assert subject.x == 15
