from unittest import TestCase

from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock


class TestPygameCollisionDetection(TestCase):
    def test_detect_right(self):
        active_blocks = [PygameGameBlock(10, 10, 20, 20),
                         PygameGameBlock(11, 11, 20, 20),
                         PygameGameBlock(12, 10, 20, 20)]
        game_blocks = [PygameGameBlock(31, 10, 20, 20)]
        detection = PygameCollisionDetection(game_blocks, active_blocks)

        assert not detection.detect(0, 0)["right"]
        assert not detection.detect(1, 0)["right"]
        assert detection.detect(2, 0)["right"]

        assert not detection.detect(0, 1)["right"]
        assert detection.detect(1, 1)["right"]
        assert detection.detect(2, 1)["right"]

    def test_detect_bottom(self):
        active_blocks = [PygameGameBlock(10, 10, 20, 20),
                         PygameGameBlock(11, 11, 20, 20),
                         PygameGameBlock(10, 12, 20, 20)]
        game_blocks = [PygameGameBlock(10, 31, 20, 20)]
        detection = PygameCollisionDetection(game_blocks, active_blocks)

        assert not detection.detect(0, 0)["bottom"]
        assert not detection.detect(1, 0)["bottom"]
        assert detection.detect(2, 0)["bottom"]

        assert not detection.detect(0, 1)["bottom"]
        assert detection.detect(1, 1)["bottom"]
        assert detection.detect(2, 1)["bottom"]

    def test_detect_left(self):
        active_blocks = [PygameGameBlock(30, 10, 20, 20),
                         PygameGameBlock(29, 11, 20, 20),
                         PygameGameBlock(28, 10, 20, 20)]
        game_blocks = [PygameGameBlock(9, 10, 20, 20)]
        detection = PygameCollisionDetection(game_blocks, active_blocks)

        assert not detection.detect(0, 0)["left"]
        assert not detection.detect(1, 0)["left"]
        assert detection.detect(2, 0)["left"]

        assert not detection.detect(0, 1)["left"]
        assert detection.detect(1, 1)["left"]
        assert detection.detect(2, 1)["left"]

    def test_detect_top(self):
        active_blocks = [PygameGameBlock(10, 30, 20, 20),
                         PygameGameBlock(11, 29, 20, 20),
                         PygameGameBlock(10, 28, 20, 20)]
        game_blocks = [PygameGameBlock(10, 9, 20, 20)]
        detection = PygameCollisionDetection(game_blocks, active_blocks)

        assert not detection.detect(0, 0)["top"]
        assert not detection.detect(1, 0)["top"]
        assert detection.detect(2, 0)["top"]

        assert not detection.detect(0, 1)["top"]
        assert detection.detect(1, 1)["top"]
        assert detection.detect(2, 1)["top"]
