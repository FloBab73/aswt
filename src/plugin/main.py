import os
import sys

import pygame

from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGraphics import PygameGraphics
from src.plugin.PygamePhysics import PygamePhysics

print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.core.GameEngine import GameEngine

pygame.init()
pygameStaticBlocks = PygameBlocksGenerator().generate()

gameEngine = GameEngine(pygameStaticBlocks, PygameGraphics(),
                        PygamePhysics(PygameCollisionDetection(pygameStaticBlocks)))
gameEngine.run()
