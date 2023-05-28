from src.adapter.BlocksGenerator import BlocksGenerator
from src.adapter.PygameEngine import PygameEngine
from src.application.GameLoop import GameLoop
from src.application.GameManager import GameManager
from src.plugin.EventHandler import EventHandler
from src.plugin.FileExtractor import FileExtractor

event_handler = EventHandler()
engine = PygameEngine(event_handler)
game_loop = GameLoop(engine, event_handler)
event_handler.add(event_handler.Events.QUIT_GAME, game_loop.quit)

GameManager(event_handler, engine, BlocksGenerator(FileExtractor()))

while game_loop.is_running:
    game_loop.run()
    engine.tick_clock(60)
    engine.fetch_events()
