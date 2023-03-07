from unittest import TestCase

from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock
from src.plugin.PygamePhysics import PygamePhysics


class TestPygamePhysics(TestCase):
    def test_move_right_against_wall(self):
        active_blocks = [PygameGameBlock(10, 10, 20, 20)]
        game_blocks = [PygameGameBlock(35, 10, 20, 20)]

        physics = PygamePhysics(PygameCollisionDetection(game_blocks, active_blocks), active_blocks)

        physics.move(0, 1, 0)
        assert active_blocks[0].x == 11
        physics.move(0, 10, 0)
        assert active_blocks[0].x == 15

    def test_gravity_and_stop(self):
        active_blocks = [PygameGameBlock(10, 10, 20, 20)]
        game_blocks = [PygameGameBlock(10, 37, 20, 20)]
        key = {
            "up": False,
            "right": False,
            "bottom": False,
            "left": False,
        }

        physics = PygamePhysics(PygameCollisionDetection(game_blocks, active_blocks), active_blocks)

        physics.movement(key)
        assert active_blocks[0].y == 11
        physics.movement(key)
        assert active_blocks[0].y == 13
        physics.movement(key)
        assert active_blocks[0].y == 16
        physics.movement(key)
        assert active_blocks[0].y == 17

    def test_jump(self):
        active_blocks = [PygameGameBlock(10, 20, 20, 20)]
        game_blocks = [PygameGameBlock(10, 40, 20, 20)]
        key_empty = {
            "up": False,
            "right": False,
            "left": False,
            "bottom": False,
        }

        key_jump = {
            "up": True,
            "right": False,
            "left": False,
            "bottom": False,
        }

        physics = PygamePhysics(PygameCollisionDetection(game_blocks, active_blocks), active_blocks)

        physics.movement(key_jump)
        assert active_blocks[0].y == 11
        physics.movement(key_empty)
        assert active_blocks[0].y == 3
        physics.movement(key_empty)
        assert active_blocks[0].y == 0
