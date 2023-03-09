import os
import sys

import pygame


# Für Daniel, damit es ohne pycharm funktioniert
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
sys.path[0] = os.getcwd()

from src.plugin.PygamePlayer import PygamePlayer
from src.plugin.PygameUserInput import PygameUserInput
from src.plugin.PygameCollisionDetection import PygameCollisionDetection
from src.plugin.PygameGraphics import PygameGraphics
from src.plugin.PygamePhysics import PygamePhysics
from src.plugin.EventHandler import EventHandler
from src.adapter.PygameBlocksGenerator import PygameBlocksGenerator
from src.core.GameEngine import GameEngine

pygame.init()
eventHandler = EventHandler()
# generate game blocks, differentiate between active and passive blocks
gameBlocks, activeBlocks = PygameBlocksGenerator().generate()
player = PygamePlayer(PygamePhysics(PygameCollisionDetection()), gameBlocks)
allBlocks = gameBlocks.copy()
allBlocks.append(player)
gameEngine = GameEngine(gameBlocks, PygameGraphics(allBlocks),
                        player, PygameUserInput())
eventHandler.add(eventHandler.Events.Health, player.modify_health)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            eventHandler(event.type)
            run = False
    clock = pygame.time.Clock()

    gameEngine.run()

    clock.tick(60)
