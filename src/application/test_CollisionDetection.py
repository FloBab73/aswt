from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection
from src.domain.GameBlock import GameBlock
from src.plugin.EventHandler import EventHandler


def initialise_collision_detection():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return CollisionDetection(game_engine, event_handler)


class TestCollisionDetection(TestCase):

    def test_detect_right_without_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(11, 11, 20, 20)
        subject2 = GameBlock(12, 10, 20, 20)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 0

        assert not detection.detect(subject1, objects, border)["right"]
        assert detection.detect(subject2, objects, border)["right"]

    def test_detect_right_with_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(10, 10, 20, 20)
        subject2 = GameBlock(11, 11, 20, 20)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 1

        assert not detection.detect(subject1, objects, border)["right"]
        assert detection.detect(subject2, objects, border)["right"]

    def test_detect_bottom_without_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(11, 11, 20, 20)
        subject2 = GameBlock(10, 12, 20, 20)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 0

        assert not detection.detect(subject1, objects, border)["bottom"]
        assert detection.detect(subject2, objects, border)["bottom"]

    def test_detect_bottom_with_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(10, 10, 20, 20)
        subject2 = GameBlock(11, 11, 20, 20)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 1

        assert not detection.detect(subject1, objects, border)["bottom"]
        assert detection.detect(subject2, objects, border)["bottom"]

    def test_detect_left_without_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(29, 11, 20, 20)
        subject2 = GameBlock(28, 10, 20, 20)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 0

        assert not detection.detect(subject1, objects, border)["left"]
        assert detection.detect(subject2, objects, border)["left"]

    def test_detect_left_with_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(30, 10, 20, 20)
        subject2 = GameBlock(29, 11, 20, 20)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 1

        assert not detection.detect(subject1, objects, border)["left"]
        assert detection.detect(subject2, objects, border)["left"]

    def test_detect_top_without_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(11, 29, 20, 20)
        subject2 = GameBlock(10, 28, 20, 20)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 0

        assert not detection.detect(subject1, objects, border)["top"]
        assert detection.detect(subject2, objects, border)["top"]

    def test_detect_top_with_border(self):
        detection = initialise_collision_detection()
        subject1 = GameBlock(10, 30, 20, 20)
        subject2 = GameBlock(11, 29, 20, 20)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 1

        assert not detection.detect(subject1, objects, border)["top"]
        assert detection.detect(subject2, objects, border)["top"]
