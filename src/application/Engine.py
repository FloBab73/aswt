class GameEngine:

    def __init__(self, event_handler):
        self.event_handler = event_handler

    def get_events(self):
        pass

    def fetch_events(self):
        pass

    def tick_clock(self, framerate):
        pass

    def get_user_input(self):
        pass

    def clipline(self, block, x1, y1, x2, y2):
        pass


class GraphicsEngine:
    def init_display(self, width, height):
        pass

    def screen_fill(self, screen, color):
        pass

    def draw_rect(self, surface, color, position):
        pass

    def draw_text(self, screen, text, position):
        pass

    def draw_button(self, screen, color, position, text):
        pass

    def update_display(self):
        pass
