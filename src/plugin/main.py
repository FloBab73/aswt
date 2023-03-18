import os
import sys

# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.core.CollisionDetection import CollisionDetection
from src.core.GraphicsEngine import GraphicsEngine
from src.core.PhysicsEngine import PhysicsEngine
from src.core.Player import Player
from src.adapter.PygameGameEngine import PygameGameEngine
from src.plugin.EventHandler import EventHandler
from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.core.GameLoop import GameLoop

event_handler = EventHandler()
game_engine = PygameGameEngine(event_handler)

# generate game blocks, differentiate between active and passive blocks
game_blocks, _ = PygameBlocksGenerator().generate()
physics = PhysicsEngine(CollisionDetection(game_engine, event_handler))
player = Player(physics, game_blocks)
all_blocks = game_blocks.copy()
active_blocks = [player]

game_loop = GameLoop(
                     game_engine,
                     game_blocks,
                     GraphicsEngine(game_engine, game_blocks, active_blocks),
                     player)

event_handler.add(event_handler.Events.Health, player.modify_health)
event_handler.add(event_handler.Events.Remove, game_loop.remove_block)

while game_loop.is_running:
    game_loop.run()
    game_engine.tick_clock(60)
    game_engine.fetch_events()
