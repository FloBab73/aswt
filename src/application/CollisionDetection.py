from enum import Enum


class Direction(Enum):
    RIGHT = 0
    BOTTOM = 1
    LEFT = 2
    TOP = 3


class CollisionDetection:

    def __init__(self, game_engine, event_handler):
        self.game_engine = game_engine
        self.event_handler = event_handler

    def detect(self, subject, objects, border_x, border_y):
        touch = set()

        for block in objects:
            if abs(block.x - subject.x) < 40 or abs(block.y - subject.y) < 40:
                if self.game_engine.clipline(block,
                                             subject.x + subject.width - 1 + border_x,
                                             subject.y,
                                             subject.x + subject.width - 1 + border_x,
                                             subject.y + subject.height - 1):
                    touch.add(Direction.RIGHT)
                    subject.touch_block(block, Direction.RIGHT)
                if self.game_engine.clipline(block,
                                             subject.x + subject.width - 1,
                                             subject.y + subject.height - 1 + border_y,
                                             subject.x,
                                             subject.y + subject.height - 1 + border_y):
                    touch.add(Direction.BOTTOM)
                    subject.touch_block(block, Direction.BOTTOM)

                if self.game_engine.clipline(block,
                                             subject.x - border_x,
                                             subject.y,
                                             subject.x - border_y,
                                             subject.y + subject.height - 1):
                    touch.add(Direction.LEFT)
                    subject.touch_block(block, Direction.LEFT)

                if self.game_engine.clipline(block,
                                             subject.x,
                                             subject.y - border_y,
                                             subject.x + subject.width - 1,
                                             subject.y - border_y):
                    touch.add(Direction.TOP)
                    subject.touch_block(block, Direction.TOP)

        return touch
