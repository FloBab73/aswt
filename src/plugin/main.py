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
gameBlocks, activeBlocks = PygameBlocksGenerator().generate()

gameEngine = GameEngine(gameBlocks, PygameGraphics(gameBlocks, activeBlocks),
                        PygamePhysics(PygameCollisionDetection(gameBlocks, activeBlocks), activeBlocks))
gameEngine.run()
