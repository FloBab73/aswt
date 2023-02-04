import os
import sys

import pygame

print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.adapter.ArrayToPygameBlocks import ArrayToPygameBlocks
from src.core.GameEngine import GameEngine

pygame.init()

blockConverter = ArrayToPygameBlocks()

gameEngine = GameEngine(blockConverter)
gameEngine.run()
