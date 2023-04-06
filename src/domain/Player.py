from datetime import datetime

from src.application.CollisionDetection import Direction
from src.domain.BlockType import BlockType
from src.domain.MovingGameBlock import MovingGameBlock


class Player(MovingGameBlock):

    def __init__(self, x=0, y=0, width=10, height=10):
        super().__init__(x, y, width, height, BlockType.PLAYER)
        self.stun = 0
        self.event_handler = None
        self.x = x
        self._startX = x
        self.y = y
        self._startY = y
        self._health = 100
        self._keys = 0
        self._last_damage_time = datetime.now()
        self.keys_str = "0"
        self.health_str = "100"

    def add_event_handler(self, event_handler):
        self.event_handler = event_handler

    def modify_health(self, modifier):
        if modifier > 0:
            self._health += modifier
        else:
            time_delta = datetime.now() - self._last_damage_time
            if modifier < 0 and time_delta.microseconds > 100_000:
                self._health += modifier
                self._last_damage_time = datetime.now()
                if self._health <= 0:
                    self.death()
        self.health_str = str(self._health)

    def touch_block(self, block, direction):
        match block.block_type:
            case BlockType.ENEMY:
                if direction == Direction.BOTTOM:
                    self.event_handler(self.event_handler.Events.KILL_ENEMY, block.x, block.y)
                else:
                    self.modify_health(-1)
                    if direction == Direction.LEFT:
                        if block.velocity_x > 0:
                            self.velocity_x = block.velocity_x * 10
                            self.stun = 20
                        else:
                            self.stun = 20
                        self.velocity_y = -self.acceleration * 2
                    if direction == Direction.RIGHT:
                        if block.velocity_x < 0:
                            self.velocity_x = block.velocity_x * 10
                            self.stun = 20
                        else:
                            self.stun = 20
                        self.velocity_y = -self.acceleration * 2
            case BlockType.ITEM_HEAL:
                self.modify_health(10)
                self.event_handler(self.event_handler.Events.REMOVE_BLOCK, block.x, block.y)
            case BlockType.ITEM_KEY:
                self.find_key()
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

    def move(self, x, y):
        self.x += x
        self.y += y

    @property
    def health(self):
        return self._health

    @property
    def keys(self):
        return self._keys

    def find_key(self):
        self._keys += 1
        self.keys_str = str(self._keys)
