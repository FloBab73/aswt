import pygame


class CollisionDetection:
    blocks = []

    def __init__(self, blocks):
        blocks.append(pygame.Rect(800, 0, 2, 600))
        blocks.append(pygame.Rect(0, 600, 800, 2))
        blocks.append(pygame.Rect(-2, 0, 2, 600))
        blocks.append(pygame.Rect(0, -2, 800, 2))
        self.blocks = blocks

    def detect(self, player, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False
        }

        for block in self.blocks:
            if block.clipline(player.x + player.w - 1 + border, player.y, player.x + player.w - 1 + border,
                              player.y + player.h - 1):
                touch["right"] = True
            if block.clipline(player.x + player.w - 1, player.y + player.h - 1 + border, player.x,
                              player.y + player.h - 1 + border):
                touch["bottom"] = True
            if block.clipline(player.x - border, player.y, player.x - border, player.y + player.h - 1):
                touch["left"] = True
            if block.clipline(player.x, player.y - border, player.x + player.w - 1, player.y - border):
                touch["top"] = True

        return touch
