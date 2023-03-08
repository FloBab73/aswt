from src.core.BlockType import BlockType
from src.core.CollisionDetection import CollisionDetection


class PygameCollisionDetection(CollisionDetection):

    def detect(self, subject, objects, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
            "hasEvent": False
        }
        for block in objects:
            if block.position().clipline(subject.x + subject.width - 1 + border,
                                         subject.y,
                                         subject.x + subject.width - 1 + border,
                                         subject.y + subject.height - 1):
                touch = self.checkBlock(touch, "right", block)
            if block.position().clipline(subject.x + subject.width - 1,
                                         subject.y + subject.height - 1 + border,
                                         subject.x,
                                         subject.y + subject.height - 1 + border):
                touch = self.checkBlock(touch, "bottom", block)
            if block.position().clipline(subject.x - border,
                                         subject.y,
                                         subject.x - border,
                                         subject.y + subject.height - 1):
                touch = self.checkBlock(touch, "left", block)
            if block.position().clipline(subject.x,
                                         subject.y - border,
                                         subject.x + subject.width - 1,
                                         subject.y - border):
                touch = self.checkBlock(touch, "top", block)

        return touch

    @staticmethod
    def checkBlock(touch, direction, block):
        if block.blockType == BlockType.ITEM_HEAL:
            touch["hasEvent"] = True
            touch["event"] = {"type": "item", "block": block}
        else:
            touch[direction] = True
        return touch
