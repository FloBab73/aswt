import pygame

from src.adapter.ArrayToPygameBlocks import ArrayToPygameBlocks
from src.core.GameEngine import GameEngine

pygame.init()

blockConverter = ArrayToPygameBlocks()

gameEngine = GameEngine(blockConverter)
gameEngine.run()
