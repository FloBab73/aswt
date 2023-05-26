from src.domain.BlockType import BlockType
from src.domain.Enemy import Enemy
from src.domain.GameBlock import GameBlock
from src.domain.Generator import Generator
from src.domain.Player import Player


class BlocksGenerator(Generator):
    def __init__(self, file_extractor):
        self.file_extractor = file_extractor
        self.block_properties = {
            (255, 216, 0): {"width": 10, "height": 10, "color": (100, 255, 0), "offset": 5,
                            "type": BlockType.ITEM_HEAL},
            (0, 38, 255): {"width": 10, "height": 10, "color": (0, 38, 200), "offset": 5, "type": BlockType.ITEM_KEY},
            (0, 255, 33): {"width": 10, "height": 10, "color": (255, 255, 255), "offset": 5, "type": BlockType.PLAYER},
            (255, 0, 0): {"width": 11, "height": 11, "color": (255, 0, 0), "offset": 5, "type": BlockType.ENEMY},
            (64, 64, 64): {"width": 20, "height": 20, "color": (64, 64, 64), "offset": 0, "type": BlockType.DOOR},
            (0, 0, 0): {"width": 20, "height": 20, "color": (100, 50, 0), "offset": 0, "type": BlockType.WALL},
        }

    def generate(self, path):
        colors = list(self.file_extractor.extract_file(path))
        game_blocks = []
        enemies = []
        player = None
        GRID_SIZE = 20

        # sort blocks with tags into arrays according to the colour
        for x_coordinate, line in enumerate(colors):
            for y_coordinate, element in enumerate(line):
                block_value = tuple(element)
                if block_value not in self.block_properties:
                    continue
                properties = self.block_properties[block_value]
                if properties["type"] == BlockType.PLAYER:
                    player = Player(
                        y_coordinate * GRID_SIZE + properties["offset"],
                        x_coordinate * GRID_SIZE + properties["offset"])
                elif properties["type"] == BlockType.ENEMY:
                    enemies.append(Enemy(
                        y_coordinate * GRID_SIZE + properties["offset"],
                        x_coordinate * GRID_SIZE + properties["offset"]))
                else:
                    game_blocks.append(GameBlock(
                        y_coordinate * GRID_SIZE + properties["offset"],
                        x_coordinate * GRID_SIZE + properties["offset"],
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
