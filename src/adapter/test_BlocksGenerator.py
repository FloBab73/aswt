from unittest import TestCase

from src.adapter.BlocksGenerator import BlocksGenerator
from src.domain.BlockType import BlockType


class MockFileExtractor:

    def extract_file(self, path):
        return [
            [[255, 255, 255],
             [255, 0, 0]],
            [[0, 0, 0],
             [0, 255, 33]]
        ]


class TestBlocksGenerator(TestCase):

    def test_generate(self):
        blocks_generator = BlocksGenerator(MockFileExtractor())

        game_blocks, enemies, player = blocks_generator.generate("path")

        assert enemies[0].block_type == BlockType.ENEMY
        assert enemies[0].x == 25
        assert enemies[0].y == 5

        assert game_blocks[0].block_type == BlockType.WALL
        assert game_blocks[0].x == 0
        assert game_blocks[0].y == 20

        assert game_blocks[1].block_type == BlockType.WALL
        assert game_blocks[1].x == -5
        assert game_blocks[1].y == -10

        assert player.block_type == BlockType.PLAYER
        assert player.x == 25
        assert player.y == 25
