from unittest import TestCase

from src.adapter.PygameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection, Direction
from src.domain.GameBlock import GameBlock
from src.domain.Player import Player
from src.plugin.EventHandler import EventHandler


def initialise_collision_detection():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return CollisionDetection(game_engine, event_handler)


class TestCollisionDetection(TestCase):

    def test_detect_right_without_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(11, 11, 20, 20)
        subject_with_contact = Player(12, 10, 20, 20)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 0

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.RIGHT not in no_contact
        assert Direction.RIGHT in contact

    def test_detect_right_with_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(10, 10, 20, 20)
        subject_with_contact = Player(11, 11, 20, 20)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 1

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.RIGHT not in no_contact
        assert Direction.RIGHT in contact

    def test_detect_bottom_without_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(11, 11, 20, 20)
        subject_with_contact = Player(10, 12, 20, 20)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 0

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.BOTTOM not in no_contact
        assert Direction.BOTTOM in contact

    def test_detect_bottom_with_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(10, 10, 20, 20)
        subject_with_contact = Player(11, 11, 20, 20)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 1

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.BOTTOM not in no_contact
        assert Direction.BOTTOM in contact

    def test_detect_left_without_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(29, 11, 20, 20)
        subject_with_contact = Player(28, 10, 20, 20)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 0

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.LEFT not in no_contact
        assert Direction.LEFT in contact

    def test_detect_left_with_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(30, 10, 20, 20)
        subject_with_contact = Player(29, 11, 20, 20)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 1

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.LEFT not in no_contact
        assert Direction.LEFT in contact

    def test_detect_top_without_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(11, 29, 20, 20)
        subject_with_contact = Player(10, 28, 20, 20)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 0

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.TOP not in no_contact
        assert Direction.TOP in contact

    def test_detect_top_with_border(self):
        detection = initialise_collision_detection()
        subject_without_contact = Player(10, 30, 20, 20)
        subject_with_contact = Player(11, 29, 20, 20)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 1

        no_contact = detection.detect(subject_without_contact, objects, border, border)
        contact = detection.detect(subject_with_contact, objects, border, border)

        assert Direction.TOP not in no_contact
        assert Direction.TOP in contact
