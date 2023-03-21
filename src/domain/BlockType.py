from enum import Enum


class BlockType(Enum):
    NONE = 0
    WALL = 1
    SECRET = 2
    PLAYER = 3
    ENEMY = 4
    NPC = 5
    ITEM_HEAL = 6
    ITEM_KEY = 7
    ITEM_VALUABLE = 8
    DOOR = 9
