from src.core.BlockType import BlockType
from src.core.CollisionDetection import CollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock


class PygameCollisionDetection(CollisionDetection):
    gameBlocks = []

    def __init__(self, gameBlocks, activeBlocks):
        super().__init__(gameBlocks, activeBlocks)
        gameBlocks.append(PygameGameBlock(800, 0, 2, 600, BlockType.WALL))
        gameBlocks.append(PygameGameBlock(0, 600, 800, 2, BlockType.WALL))
        gameBlocks.append(PygameGameBlock(-2, 0, 2, 600, BlockType.WALL))
        gameBlocks.append(PygameGameBlock(0, -2, 800, 2, BlockType.WALL))

    def detect(self, index, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
            "hasEvent": False
        }
        subject = self.activeBlocks[index]
        for block in self.gameBlocks:
            if block.position().clipline(subject.x + subject.width - 1 + border, subject.y,
                                         subject.x + subject.width - 1 + border,
                                         subject.y + subject.height - 1):
                touch = self.checkBlock(touch, "right", block)
            if block.position().clipline(subject.x + subject.width - 1, subject.y + subject.height - 1 + border,
                                         subject.x,
                                         subject.y + subject.height - 1 + border):
                touch = self.checkBlock(touch, "bottom", block)
            if block.position().clipline(subject.x - border, subject.y, subject.x - border,
                                         subject.y + subject.height - 1):
                touch = self.checkBlock(touch, "left", block)
            if block.position().clipline(subject.x, subject.y - border, subject.x + subject.width - 1,
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
