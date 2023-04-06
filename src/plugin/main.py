import os
import sys

from src.domain.Level import Level

# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.adapter.PygameGameEngine import PygameGameEngine
from src.plugin.EventHandler import EventHandler
from src.application.GameLoop import GameLoop
from src.application.GameManager import GameManager

event_handler = EventHandler()
game_engine = PygameGameEngine(event_handler)
game_loop = GameLoop(game_engine, event_handler)
event_handler.add(event_handler.Events.QUIT_GAME, game_loop.quit)

manger = GameManager(event_handler, game_engine)

while game_loop.is_running:
    game_loop.run()
    game_engine.tick_clock(60)
    game_engine.fetch_events()
