class GameLoop:

    def __init__(self, game_engine, event_handler):
        self.event_handler = event_handler
        self.game_engine = game_engine
        self.is_running = True

    def run(self):
        self.game_engine.get_user_input()
        self.event_handler(self.event_handler.Events.MOVE_ENEMIES)
        self.event_handler(self.event_handler.Events.DRAW)

    def quit(self):
        self.is_running = False
