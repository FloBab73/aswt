from unittest import TestCase

from src.adapter.PygameGameEngine import PygameGameEngine
from src.application.CollisionDetection import CollisionDetection
from src.application.PhysicsEngine import PhysicsEngine
from src.domain.BlockType import BlockType
from src.domain.GameBlock import GameBlock
from src.domain.Level import Level
from src.domain.MovingGameBlock import MovingGameBlock
from src.domain.Player import Player
from src.plugin.EventHandler import EventHandler


def initialise_physics():
    event_handler = EventHandler()
    game_engine = PygameGameEngine(event_handler)
    return PhysicsEngine(CollisionDetection(game_engine, event_handler), None)


class TestPhysics(TestCase):

    def test_move_right(self):
        physics = initialise_physics()
        subject = MovingGameBlock(10, 10, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(35, 10, 20, 20)]

        physics.move(subject, objects, 1, 0)
        assert subject.x == 11

    def test_move_against_wall(self):
        physics = initialise_physics()
        subject = MovingGameBlock(10, 10, 20, 20, BlockType.PLAYER)
        objects = [GameBlock(35, 10, 20, 20)]

        physics.move(subject, objects, 10, 0)
        assert subject.x == 15

    def test_player_gravity_and_stop(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine(event_handler)
        collision_detection = CollisionDetection(game_engine, event_handler)
        player = Player()
        level = Level(event_handler, [GameBlock(0, 17, 20, 20)], [], player)
        physics_engine = PhysicsEngine(collision_detection, level)

        physics_engine.move_player(False, False, False)
        assert player.y == 1
        physics_engine.move_player(False, False, False)
        assert player.y == 3
        physics_engine.move_player(False, False, False)
        assert player.y == 6
        physics_engine.move_player(False, False, False)
        assert player.y == 7

    def test_player_jump(self):
        event_handler = EventHandler()
        game_engine = PygameGameEngine(event_handler)
        collision_detection = CollisionDetection(game_engine, event_handler)
        player = Player(0, 20)
        level = Level(event_handler, [GameBlock(0, 30, 20, 20), GameBlock(0, -5, 20, 5)], [], player)
        physics_engine = PhysicsEngine(collision_detection, level)

        physics_engine.move_player(False, True, False)
        assert player.y == 11
        physics_engine.move_player(False, False, False)
        assert player.y == 3
        physics_engine.move_player(False, False, False)
        assert player.y == 0