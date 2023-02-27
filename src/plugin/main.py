import os
import sys

import pygame

# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGraphics import PygameGraphics
from src.plugin.PygamePhysics import PygamePhysics
from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.core.GameEngine import GameEngine

pygame.init()
# generate game blocks, differentiate between active and passive blocks
gameBlocks, activeBlocks = PygameBlocksGenerator().generate()

gameEngine = GameEngine(gameBlocks, PygameGraphics(gameBlocks, activeBlocks),
                        PygamePhysics(PygameCollisionDetection(gameBlocks, activeBlocks), activeBlocks))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock = pygame.time.Clock()

    gameEngine.run()

    clock.tick(60)
