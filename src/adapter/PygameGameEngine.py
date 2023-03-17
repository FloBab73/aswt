import pygame

from src.core.GameEngine import GameEngine


class PygameGameEngine(GameEngine):

    def __init__(self):
        super().__init__()
        pygame.init()
        self.clock = pygame.time.Clock()

    def tick_clock(self, framerate):
        self.clock.tick(framerate)

    def get_user_input(self):
        key = {
            "up": False,
            "right": False,
            "left": False,
            "bottom": False,
        }
        pygame_key = pygame.key.get_pressed()

        if pygame_key[pygame.K_UP]:
            key["up"] = True
        if pygame_key[pygame.K_RIGHT]:
            key["right"] = True
        if pygame_key[pygame.K_DOWN]:
            key["down"] = True
        if pygame_key[pygame.K_LEFT]:
            key["left"] = True

        return key

    def clipline(self, block, x1, y1, x2, y2):
        pygame_block = pygame.Rect(block.position())
        return pygame_block.clipline(x1, y2, x2, y2)

    def init_display(self, width, height):
        return pygame.display.set_mode((width, height))

    def screen_fill(self, screen, color):
        screen.fill(color)

    def draw_rect(self, surface, color, position):
        pygame.draw.rect(surface, color, position)

    def update_display(self):
        pygame.display.update()
