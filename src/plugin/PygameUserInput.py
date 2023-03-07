import pygame

from src.core.UserInput import UserInput


class PygameUserInput(UserInput):
    def getUserInput(self):
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
