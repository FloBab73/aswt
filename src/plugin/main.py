import os
import sys

from src.domain.Level import Level

# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.application.CollisionDetection import CollisionDetection
from src.application.GraphicsEngine import GraphicsEngine
from src.application.PhysicsEngine import PhysicsEngine
from src.adapter.PygameGameEngine import PygameGameEngine
from src.plugin.EventHandler import EventHandler
from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.application.GameLoop import GameLoop

event_handler = EventHandler()
game_engine = PygameGameEngine(event_handler)

static_blocks, enemies, player = PygameBlocksGenerator().generate()
level = Level(event_handler, static_blocks, enemies, player)

physics = PhysicsEngine(CollisionDetection(game_engine, event_handler), level)
event_handler.add(event_handler.Events.MOVE_PLAYER, physics.move_player)
event_handler.add(event_handler.Events.MOVE_ENEMIES, physics.move_enemies)

graphics = GraphicsEngine(game_engine, level)
event_handler.add(event_handler.Events.DRAW, graphics.draw)

game_loop = GameLoop(game_engine, event_handler)
event_handler.add(event_handler.Events.QUIT, game_loop.quit)

while game_loop.is_running:
    game_loop.run()
    game_engine.tick_clock(60)
    game_engine.fetch_events()
