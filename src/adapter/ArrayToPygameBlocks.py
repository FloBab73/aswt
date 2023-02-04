from src.core.Generator import Generator
from src.plugin import extractor
from src.plugin.GameBlock import GameBlock


class ArrayToPygameBlocks(Generator):
    def generate(self):
        array = list(extractor.extract())
        result = []

        for x in range(len(array)):
            for y in range(len(array[0])):
                if array[x][y] == 1:
                    result.append(GameBlock(y * 20, x * 20, 20, 20, GameBlock.WALL))
        return result
