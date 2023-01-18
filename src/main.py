import sys
import pygame

from src import generator
from src.PhysicsEngine import PhysicsEngine
from src.GraphicsEngine import GraphicsEngine

pygame.init()
clock = pygame.time.Clock()
player = pygame.Rect(350, 0, 10, 10)
blocks = generator.generate()

pEngine = PhysicsEngine(blocks)
gEngine = GraphicsEngine(blocks)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player = pEngine.movement(player)
    gEngine.draw(player)

    clock.tick(60)
