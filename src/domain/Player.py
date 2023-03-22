from src.domain.BlockType import BlockType
from src.domain.MovingGameBlock import MovingGameBlock


class Player(MovingGameBlock):

    def __init__(self, x=0, y=0, width=10, height=10):
        super().__init__(x, y, width, height, BlockType.PLAYER)
        self.event_handler = None
        self.x = x
        self._startX = x
        self.y = y
        self._startY = y
        self._health = 100
        self._keys = 0

    def add_event_handler(self, event_handler):
        self.event_handler = event_handler

    def modify_health(self, modifier):
        self._health += modifier
        if self._health <= 0:
            self.death()

    def death(self):
        self.event_handler(self.event_handler.Events.DEATH)
        print("X.X Du bist Tot X.X")

    def resetPos(self):
        self.x = self._startX
        self.y = self._startY
        self._health = 100

    @property
    def health(self):
        return self._health

    @property
    def keys(self):
        return self._keys

    def find_key(self):
        self._keys += 1
