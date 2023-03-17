import os
import sys

# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.adapter.PygameGameEngine import PygameGameEngine
from src.plugin.PygamePlayer import PygamePlayer
from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGraphics import PygameGraphics
from src.plugin.PygamePhysics import PygamePhysics
from src.plugin.EventHandler import EventHandler
from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.core.GameLoop import GameLoop

game_engine = PygameGameEngine()

event_handler = EventHandler()

# generate game blocks, differentiate between active and passive blocks
game_blocks, _ = PygameBlocksGenerator().generate()
physics = PygamePhysics(PygameCollisionDetection(game_engine, event_handler))
player = PygamePlayer(physics, game_blocks)
all_blocks = game_blocks.copy()
active_blocks = [player]

game_loop = GameLoop(game_engine, game_blocks, PygameGraphics(game_engine, game_blocks, active_blocks),
                     player)

event_handler.add(event_handler.Events.Health, player.modify_health)
event_handler.add(event_handler.Events.Remove, game_loop.remove_block)

run = True
while run:
    for event in game_engine.get_events():
        if event == "QUIT":
            event_handler(event.type)
            run = False

    game_loop.run()

    game_engine.tick_clock(60)
