from src.application.CollisionDetection import Direction
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

    def touch_block(self, block, direction):
        match block.block_type:
            case BlockType.ENEMY:
                if direction == Direction.BOTTOM:
                    self.event_handler(self.event_handler.Events.KILL_ENEMY, block.x, block.y)
                else:
                    self.modify_health(-1)
            case BlockType.ITEM_HEAL:
                self.modify_health(10)
                self.event_handler(self.event_handler.Events.REMOVE_BLOCK, block.x, block.y)
            case BlockType.ITEM_KEY:
                self._keys += 1
                self.event_handler(self.event_handler.Events.REMOVE_BLOCK, block.x, block.y)
            case BlockType.DOOR:
                self.event_handler(self.event_handler.Events.DOOR)

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
