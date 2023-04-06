from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection, Direction
from src.domain.BlockType import BlockType
from src.domain.GameBlock import GameBlock
from src.domain.MovingGameBlock import MovingGameBlock
from src.plugin.EventHandler import EventHandler


def initialise_collision_detection():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return CollisionDetection(game_engine, event_handler)


class TestCollisionDetection(TestCase):

    def test_detect_right_without_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(11, 11, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(12, 10, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 0

        assert Direction.RIGHT not in detection.detect(subject1, objects, border, border)
        assert Direction.RIGHT in detection.detect(subject2, objects, border, border)

    def test_detect_right_with_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(10, 10, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(11, 11, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(31, 10, 20, 20)]
        border = 1

        assert Direction.RIGHT not in detection.detect(subject1, objects, border, border)
        assert Direction.RIGHT in detection.detect(subject2, objects, border, border)

    def test_detect_bottom_without_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(11, 11, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(10, 12, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 0

        assert Direction.BOTTOM not in detection.detect(subject1, objects, border, border)
        assert Direction.BOTTOM in detection.detect(subject2, objects, border, border)

    def test_detect_bottom_with_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(10, 10, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(11, 11, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(10, 31, 20, 20)]
        border = 1

        assert Direction.BOTTOM not in detection.detect(subject1, objects, border, border)
        assert Direction.BOTTOM in detection.detect(subject2, objects, border, border)

    def test_detect_left_without_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(29, 11, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(28, 10, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 0

        assert Direction.LEFT not in detection.detect(subject1, objects, border, border)
        assert Direction.LEFT in detection.detect(subject2, objects, border, border)

    def test_detect_left_with_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(30, 10, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(29, 11, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(9, 10, 20, 20)]
        border = 1

        assert Direction.LEFT not in detection.detect(subject1, objects, border, border)
        assert Direction.LEFT in detection.detect(subject2, objects, border, border)

    def test_detect_top_without_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(11, 29, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(10, 28, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 0

        assert Direction.TOP not in detection.detect(subject1, objects, border, border)
        assert Direction.TOP in detection.detect(subject2, objects, border, border)

    def test_detect_top_with_border(self):
        detection = initialise_collision_detection()
        subject1 = MovingGameBlock(10, 30, 20, 20, BlockType.PLAYER)
        subject2 = MovingGameBlock(11, 29, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(10, 9, 20, 20)]
        border = 1

        assert Direction.TOP not in detection.detect(subject1, objects, border, border)
        assert Direction.TOP in detection.detect(subject2, objects, border, border)
