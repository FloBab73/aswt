from src.adapter.BlocksGenerator import BlocksGenerator
from src.adapter.PygameGameEngine import PygameGameEngine
from src.application.GameLoop import GameLoop
from src.application.GameManager import GameManager
from src.plugin.EventHandler import EventHandler
from src.plugin.FileExtractor import FileExtractor

event_handler = EventHandler()
game_engine = PygameGameEngine(event_handler)
game_loop = GameLoop(game_engine, event_handler)
event_handler.add(event_handler.Events.QUIT_GAME, game_loop.quit)

GameManager(event_handler, game_engine, BlocksGenerator(FileExtractor()))

while game_loop.is_running:
    game_loop.run()
    game_engine.tick_clock(60)
    game_engine.fetch_events()
