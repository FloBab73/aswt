from src.core.CollisionDetection import CollisionDetection
from src.plugin.PygameGameBlock import PygameGameBlock


class PygameCollisionDetection(CollisionDetection):
    blocks = []

    def __init__(self, blocks):
        super().__init__(blocks)
        blocks.append(PygameGameBlock(800, 0, 2, 600, PygameGameBlock.WALL))
        blocks.append(PygameGameBlock(0, 600, 800, 2, PygameGameBlock.WALL))
        blocks.append(PygameGameBlock(-2, 0, 2, 600, PygameGameBlock.WALL))
        blocks.append(PygameGameBlock(0, -2, 800, 2, PygameGameBlock.WALL))
        self.dummyBlock = PygameGameBlock(0, 0, 0, 0)

    def detect(self, player, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
            "hasEvent": False
        }

        for block in self.blocks:
            if block.pygameBlock.clipline(player.x + player.w - 1 + border, player.y,
                                          player.x + player.w - 1 + border,
                                          player.y + player.h - 1):
                touch = self.checkBlock(touch, "right", block)
            if block.pygameBlock.clipline(player.x + player.w - 1, player.y + player.h - 1 + border, player.x,
                                          player.y + player.h - 1 + border):
                touch = self.checkBlock(touch, "bottom", block)
            if block.pygameBlock.clipline(player.x - border, player.y, player.x - border, player.y + player.h - 1):
                touch = self.checkBlock(touch, "left", block)
            if block.pygameBlock.clipline(player.x, player.y - border, player.x + player.w - 1, player.y - border):
                touch = self.checkBlock(touch, "top", block)

        return touch

    @staticmethod
    def checkBlock(touch, direction, block):
        if block.blockType == PygameGameBlock.ITEM:
            touch["hasEvent"] = True
            touch["event"] = {"type": "item", "block": block}
        else:
            touch[direction] = True
        return touch
