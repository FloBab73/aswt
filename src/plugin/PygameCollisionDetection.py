from src.core.BlockType import BlockType
from src.core.CollisionDetection import CollisionDetection


class PygameCollisionDetection(CollisionDetection):
    def __init__(self, event_handler):
        self.event_handler = event_handler

    def detect(self, subject, objects, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
        }
        for block in objects:
            if block.position().clipline(subject.x + subject.width - 1 + border,
                                         subject.y,
                                         subject.x + subject.width - 1 + border,
                                         subject.y + subject.height - 1):
                touch = self.check_block(touch, "right", block)
            if block.position().clipline(subject.x + subject.width - 1,
                                         subject.y + subject.height - 1 + border,
                                         subject.x,
                                         subject.y + subject.height - 1 + border):
                touch = self.check_block(touch, "bottom", block)
            if block.position().clipline(subject.x - border,
                                         subject.y,
                                         subject.x - border,
                                         subject.y + subject.height - 1):
                touch = self.check_block(touch, "left", block)
            if block.position().clipline(subject.x,
                                         subject.y - border,
                                         subject.x + subject.width - 1,
                                         subject.y - border):
                touch = self.check_block(touch, "top", block)

        return touch

    def check_block(self, touch, direction, block):
        if block.block_type == BlockType.ITEM_HEAL:
            self.event_handler.__call__(self.event_handler.Events.Health, 10)
            self.event_handler.__call__(self.event_handler.Events.Remove, block.position().x, block.position().y)

        else:
            touch[direction] = True
        return touch
