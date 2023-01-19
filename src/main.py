import sys
import os
import pygame

import generator
from PhysicsEngine import PhysicsEngine
from GraphicsEngine import GraphicsEngine

if os.path.basename(os.getcwd()) == "src":
    os.chdir("../")

pygame.init()
clock = pygame.time.Clock()
player = pygame.Rect(0, 0, 10, 10)
blocks = generator.generate()

pEngine = PhysicsEngine(blocks)
gEngine = GraphicsEngine(blocks)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player = pEngine.movement(player)
    gEngine.draw(player)

    clock.tick(60)
