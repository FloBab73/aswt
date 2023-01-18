
import pygame

from src.adapter.ArrayToPygameBlocks import ArrayToPygameBlocks
from src.core.GameEngine import GameEngine

pygame.init()

atpb = ArrayToPygameBlocks()

ge = GameEngine(atpb)
ge.run()