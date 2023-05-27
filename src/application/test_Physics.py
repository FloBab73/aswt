from unittest import TestCase

from src.adapter.PygameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection
from src.application.Physics import Physics
from src.domain.GameBlock import GameBlock
from src.domain.Level import Level
from src.domain.Player import Player
from src.plugin.EventHandler import EventHandler


def initialise_physics():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return Physics(CollisionDetection(game_engine, event_handler), None)


class TestPhysics(TestCase):

    def test_move_right(self):
        physics = initialise_physics()
        subject = Player(10, 10, 20, 20)

        physics.block_mover.move_block(subject, [], 1, 0)

        assert subject.x == 11

    def test_move_right_against_wall(self):
        physics = initialise_physics()
        subject = Player(10, 10, 20, 20)
        objects = [GameBlock(35, 10, 20, 20)]

        physics.block_mover.move_block(subject, objects, 10, 0)

        assert subject.x == 15

    def test_move_left_against_wall(self):
        physics = initialise_physics()
        subject = Player(25, 0, 20, 20)
        objects = [GameBlock(0, 0, 20, 20)]

        physics.block_mover.move_block(subject, objects, -15, 0)

        assert subject.x == 20

    def test_player_gravity_and_stop(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine(event_handler)
        collision_detection = CollisionDetection(game_engine, event_handler)
        player = Player(0, 0)
        level = Level(event_handler, [GameBlock(0, 15, 20, 20)], [], player)
        physics_engine = Physics(collision_detection, level)

        physics_engine.move_player(False, False, False)
        assert player.y == 1
        physics_engine.move_player(False, False, False)
        assert player.y == 3
        physics_engine.move_player(False, False, False)
        assert player.y == 5

    def test_player_jump(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine(event_handler)
        collision_detection = CollisionDetection(game_engine, event_handler)
        player = Player(0, 20)
        level = Level(event_handler, [GameBlock(0, 30, 20, 20), GameBlock(0, -5, 20, 5)], [], player)
        physics_engine = Physics(collision_detection, level)

        physics_engine.move_player(False, True, False)
        assert player.y == 11
        physics_engine.move_player(False, False, False)
        assert player.y == 3
        physics_engine.move_player(False, False, False)
        assert player.y == 0
