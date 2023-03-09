from unittest import TestCase

from src.plugin.EventHandler import EventHandler
from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock


class TestPygameCollisionDetection(TestCase):
    def test_detect_right(self):
        event_handler = EventHandler()
        subject1 = PygameGameBlock(10, 10, 20, 20)
        subject2 = PygameGameBlock(11, 11, 20, 20)
        subject3 = PygameGameBlock(12, 10, 20, 20)
        objects = [PygameGameBlock(31, 10, 20, 20)]
        detection = PygameCollisionDetection(event_handler)

        assert not detection.detect(subject1, objects, 0)["right"]
        assert not detection.detect(subject2, objects, 0)["right"]
        assert detection.detect(subject3, objects, 0)["right"]

        assert not detection.detect(subject1, objects, 1)["right"]
        assert detection.detect(subject2, objects, 1)["right"]
        assert detection.detect(subject3, objects, 1)["right"]

    def test_detect_bottom(self):
        event_handler = EventHandler()
        subject1 = PygameGameBlock(10, 10, 20, 20)
        subject2 = PygameGameBlock(11, 11, 20, 20)
        subject3 = PygameGameBlock(10, 12, 20, 20)
        objects = [PygameGameBlock(10, 31, 20, 20)]
        detection = PygameCollisionDetection(event_handler)

        assert not detection.detect(subject1, objects, 0)["bottom"]
        assert not detection.detect(subject2, objects, 0)["bottom"]
        assert detection.detect(subject3, objects, 0)["bottom"]

        assert not detection.detect(subject1, objects, 1)["bottom"]
        assert detection.detect(subject2, objects, 1)["bottom"]
        assert detection.detect(subject3, objects, 1)["bottom"]

    def test_detect_left(self):
        event_handler = EventHandler()
        subject1 = PygameGameBlock(30, 10, 20, 20)
        subject2 = PygameGameBlock(29, 11, 20, 20)
        subject3 = PygameGameBlock(28, 10, 20, 20)
        objects = [PygameGameBlock(9, 10, 20, 20)]
        detection = PygameCollisionDetection(event_handler)

        assert not detection.detect(subject1, objects, 0)["left"]
        assert not detection.detect(subject2, objects, 0)["left"]
        assert detection.detect(subject3, objects, 0)["left"]

        assert not detection.detect(subject1, objects, 1)["left"]
        assert detection.detect(subject2, objects, 1)["left"]
        assert detection.detect(subject3, objects, 1)["left"]

    def test_detect_top(self):
        event_handler = EventHandler()
        subject1 = PygameGameBlock(10, 30, 20, 20)
        subject2 = PygameGameBlock(11, 29, 20, 20)
        subject3 = PygameGameBlock(10, 28, 20, 20)
        objects = [PygameGameBlock(10, 9, 20, 20)]
        detection = PygameCollisionDetection(event_handler)

        assert not detection.detect(subject1, objects, 0)["top"]
        assert not detection.detect(subject2, objects, 0)["top"]
        assert detection.detect(subject3, objects, 0)["top"]

        assert not detection.detect(subject1, objects, 1)["top"]
        assert detection.detect(subject2, objects, 1)["top"]
        assert detection.detect(subject3, objects, 1)["top"]
