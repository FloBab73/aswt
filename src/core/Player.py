from src.core.BlockType import BlockType
from src.core.GameBlock import GameBlock


class Player:

    def __init__(self, x, y, w, h):
        self.pos = GameBlock(x, y, w, h, BlockType.PLAYER)
        self._health = 100

    def position(self):
        return [self.pos.x, self.pos.y, self.pos.width, self.pos.height]

    def modify_health(self, modifier):
        self._health += modifier
        print ("Player Health: ", self._health)
        if self._health <= 0:
            self.death()

    def death(self):
        print ("X.X Du bist Tot X.X")