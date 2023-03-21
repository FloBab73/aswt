import pygame

from src.application.GameEngine import GameEngine


class PygameGameEngine(GameEngine):

    def __init__(self, event_handler):
        super().__init__()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.event_handler = event_handler
        self.font = pygame.font.SysFont(None, 30)

    def tick_clock(self, framerate):
        self.clock.tick(framerate)

    def fetch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.event_handler(self.event_handler.Events.QUIT)

    def get_user_input(self):
        up = False
        right = False
        left = False
        down = False
        esc = False

        pygame_key = pygame.key.get_pressed()

        if pygame_key[pygame.K_UP]:
            up = True
        if pygame_key[pygame.K_RIGHT]:
            right = True
        if pygame_key[pygame.K_DOWN]:
            down = True
        if pygame_key[pygame.K_LEFT]:
            left = True
        if pygame_key[pygame.K_r]:
            self.event_handler(self.event_handler.Events.RESET)
        if pygame_key[pygame.K_ESCAPE]:
            self.event_handler(self.event_handler.Events.QUIT)

        self.event_handler(self.event_handler.Events.MOVE_PLAYER, left, up, right)
        # self.event_handler(self.event_handler.Events.KEY_PRESSED, up, right, down, left)

    def clipline(self, block, x1, y1, x2, y2):
        pygame_block = pygame.Rect(block.position())
        return pygame_block.clipline(x1, y1, x2, y2)

    def init_display(self, width, height):
        return pygame.display.set_mode((width, height))

    def screen_fill(self, screen, color):
        screen.fill(color)

    def draw_rect(self, surface, color, position):
        pygame.draw.rect(surface, color, position)

    def draw_text(self, screen, text, position):
        img = self.font.render(text, True, [200, 200, 200])
        screen.blit(img, position)

    def update_display(self):
        pygame.display.update()
