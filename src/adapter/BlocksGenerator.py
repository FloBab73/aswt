from src.domain.BlockType import BlockType
from src.domain.Enemy import Enemy
from src.domain.GameBlock import GameBlock
from src.domain.Generator import Generator
from src.domain.Player import Player
from src.plugin import FileExtractor


class BlocksGenerator(Generator):
    def __init__(self):
        self.block_properties = {
            (255, 216, 0): {"width": 10, "height": 10, "color": (100, 255, 0), "offset": 5, "type": BlockType.ITEM_HEAL},
            (0,  38, 255): {"width": 10, "height": 10, "color": (0,  38, 200), "offset": 5, "type": BlockType.ITEM_KEY},
            (0, 255,  33): {"width": 10, "height": 10, "color": (255, 255, 255), "offset": 5, "type": BlockType.PLAYER},
            (255, 0,   0): {"width": 11, "height": 11, "color": (255,   0, 0), "offset": 5, "type": BlockType.ENEMY},
            (64, 64,  64): {"width": 20, "height": 20, "color": (64,  64, 64), "offset": 0, "type": BlockType.DOOR},
            (0,   0,   0): {"width": 20, "height": 20, "color": (100, 50,  0), "offset": 0, "type": BlockType.WALL},
        }

    def generate(self, path):
        array = list(FileExtractor.extract_file(path))
        game_blocks = []
        enemies = []
        player = None

        # sort blocks with tags into arrays according to the colour
        for x in range(len(array)):
            for y in range(len(array[0])):
                block_value = tuple(array[x][y])
                if block_value in self.block_properties:
                    properties = self.block_properties[block_value]
                    if properties["type"] == BlockType.PLAYER:
                        player = Player(y * 20 + 5, x * 20 + 5, 10, 10)
                    else:
                        if properties["type"] == BlockType.ENEMY:
                            enemies.append(Enemy(y * 20 + 5, x * 20 + 5, properties["width"], properties["height"]))
                        else:
                            game_blocks.append(GameBlock(
                                                            y * 20 + properties["offset"],
                                                            x * 20 + properties["offset"],
                                                            properties["width"],
                                                            properties["height"],
                                                            properties["color"],
                                                            properties["type"]
                                                        )
                                               )
        game_blocks.append(GameBlock(-5, -10, 810, 10, block_type=BlockType.WALL))  # top
        game_blocks.append(GameBlock(800, -5, 5, 610, block_type=BlockType.WALL))  # right
        game_blocks.append(GameBlock(-2, 600, 804, 20, block_type=BlockType.WALL))  # bottom
        game_blocks.append(GameBlock(-5, -5, 5, 610, block_type=BlockType.WALL))  # left
        return game_blocks, enemies, player
