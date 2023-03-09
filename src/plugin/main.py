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
event_handler = EventHandler()

# generate game blocks, differentiate between active and passive blocks
game_blocks, _ = PygameBlocksGenerator().generate()
physics = PygamePhysics(PygameCollisionDetection(event_handler))
player = PygamePlayer(physics, game_blocks)
all_blocks = game_blocks.copy()
active_blocks = [player]

game_engine = GameEngine(game_blocks, PygameGraphics(game_blocks, active_blocks),
                         player, PygameUserInput())

event_handler.add(event_handler.Events.Health, player.modify_health)
event_handler.add(event_handler.Events.Remove, game_engine.remove_block)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_handler(event.type)
            run = False
    clock = pygame.time.Clock()

    game_engine.run()

    clock.tick(60)
