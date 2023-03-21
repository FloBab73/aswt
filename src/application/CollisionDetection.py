from src.domain.BlockType import BlockType


class CollisionDetection:

    def __init__(self, game_engine, event_handler):
        self.game_engine = game_engine
        self.event_handler = event_handler

    def detect(self, subject, objects, border):
        # TODO replcse Dict with list
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
        }
        for block in objects:
            if self.game_engine.clipline(block,
                                         subject.x + subject.width - 1 + border,
                                         subject.y,
                                         subject.x + subject.width - 1 + border,
                                         subject.y + subject.height - 1):
                touch = self.check_block(touch, "right", block)
            if self.game_engine.clipline(block,
                                         subject.x + subject.width - 1,
                                         subject.y + subject.height - 1 + border,
                                         subject.x,
                                         subject.y + subject.height - 1 + border):
                touch = self.check_block(touch, "bottom", block)
            if self.game_engine.clipline(block,
                                         subject.x - border,
                                         subject.y,
                                         subject.x - border,
                                         subject.y + subject.height - 1):
                touch = self.check_block(touch, "left", block)
            if self.game_engine.clipline(block,
                                         subject.x,
                                         subject.y - border,
                                         subject.x + subject.width - 1,
                                         subject.y - border):
                touch = self.check_block(touch, "top", block)

        return touch

    def check_block(self, touch, direction, block):
        if block.block_type == BlockType.ITEM_HEAL:
            self.event_handler(self.event_handler.Events.Health, 10)
            self.event_handler(self.event_handler.Events.Remove, block.x, block.y)
        elif block.block_type == BlockType.ITEM_KEY:
            self.event_handler(self.event_handler.Events.Key)
            self.event_handler(self.event_handler.Events.Remove, block.x, block.y)
        elif block.block_type == BlockType.DOOR:
            self.event_handler(self.event_handler.Events.Door)
        else:
            touch[direction] = True
        return touch
