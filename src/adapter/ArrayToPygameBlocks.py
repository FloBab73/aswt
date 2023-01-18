import pygame.draw

from src.core.Generator import Generator
from src.plugin import extractor


class ArrayToPygameBlocks(Generator):
    def generate(self):
        array = list(extractor.extract())
        result = []

        for x in range(len(array)):
            for y in range(len(array[0])):
                if array[x][y] == 1:
                    result.append(pygame.Rect(y * 20, x * 20, 20, 20))
        return result
