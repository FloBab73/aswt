from unittest import TestCase

from src.plugin.EventHandler import EventHandler
from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock
from src.plugin.PygamePhysics import PygamePhysics


class TestPygamePhysics(TestCase):
    def test_move_right_against_wall(self):
        event_handler = EventHandler()
        subject = PygameGameBlock(10, 10, 20, 20)
        objects = [PygameGameBlock(35, 10, 20, 20)]

        physics = PygamePhysics(PygameCollisionDetection(event_handler))

        physics.move(subject, objects, 1, 0)
        assert subject.x == 11
        physics.move(subject, objects, 10, 0)
        assert subject.x == 15
