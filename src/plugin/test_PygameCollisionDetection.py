from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.core.CollisionDetection import CollisionDetection
from src.core.GameBlock import GameBlock
from src.plugin.EventHandler import EventHandler


class TestCollisionDetection(TestCase):
    def test_detect_right(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()
        subject1 = GameBlock(10, 10, 20, 20)
        subject2 = GameBlock(11, 11, 20, 20)
        subject3 = GameBlock(12, 10, 20, 20)
        objects = [GameBlock(31, 10, 20, 20)]
        detection = CollisionDetection(game_engine, event_handler)

        assert not detection.detect(subject1, objects, 0)["right"]
        assert not detection.detect(subject2, objects, 0)["right"]
        assert detection.detect(subject3, objects, 0)["right"]

        assert not detection.detect(subject1, objects, 1)["right"]
        assert detection.detect(subject2, objects, 1)["right"]
        assert detection.detect(subject3, objects, 1)["right"]

    def test_detect_bottom(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()

        subject1 = GameBlock(10, 10, 20, 20)
        subject2 = GameBlock(11, 11, 20, 20)
        subject3 = GameBlock(10, 12, 20, 20)
        objects = [GameBlock(10, 31, 20, 20)]
        detection = CollisionDetection(game_engine, event_handler)

        assert not detection.detect(subject1, objects, 0)["bottom"]
        assert not detection.detect(subject2, objects, 0)["bottom"]
        assert detection.detect(subject3, objects, 0)["bottom"]

        assert not detection.detect(subject1, objects, 1)["bottom"]
        assert detection.detect(subject2, objects, 1)["bottom"]
        assert detection.detect(subject3, objects, 1)["bottom"]

    def test_detect_left(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()

        subject1 = GameBlock(30, 10, 20, 20)
        subject2 = GameBlock(29, 11, 20, 20)
        subject3 = GameBlock(28, 10, 20, 20)
        objects = [GameBlock(9, 10, 20, 20)]
        detection = CollisionDetection(game_engine, event_handler)

        assert not detection.detect(subject1, objects, 0)["left"]
        assert not detection.detect(subject2, objects, 0)["left"]
        assert detection.detect(subject3, objects, 0)["left"]

        assert not detection.detect(subject1, objects, 1)["left"]
        assert detection.detect(subject2, objects, 1)["left"]
        assert detection.detect(subject3, objects, 1)["left"]

    def test_detect_top(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine()

        subject1 = GameBlock(10, 30, 20, 20)
        subject2 = GameBlock(11, 29, 20, 20)
        subject3 = GameBlock(10, 28, 20, 20)
        objects = [GameBlock(10, 9, 20, 20)]
        detection = CollisionDetection(game_engine, event_handler)

        assert not detection.detect(subject1, objects, 0)["top"]
        assert not detection.detect(subject2, objects, 0)["top"]
        assert detection.detect(subject3, objects, 0)["top"]

        assert not detection.detect(subject1, objects, 1)["top"]
        assert detection.detect(subject2, objects, 1)["top"]
        assert detection.detect(subject3, objects, 1)["top"]
