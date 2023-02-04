from src.plugin.GameBlock import GameBlock


def checkBlock(touch, direction, block):
    if block.blockType == GameBlock.ITEM:
        touch["hasEvent"] = True
        touch["event"] = {"type": "item", "block": block}
    else:
        touch[direction] = True
    return touch


class CollisionDetection:
    blocks = []

    def __init__(self, blocks):
        blocks.append(GameBlock(800, 0, 2, 600, GameBlock.WALL))
        blocks.append(GameBlock(0, 600, 800, 2, GameBlock.WALL))
        blocks.append(GameBlock(-2, 0, 2, 600, GameBlock.WALL))
        blocks.append(GameBlock(0, -2, 800, 2, GameBlock.WALL))
        blocks.append(GameBlock(300, 30, 10, 10, GameBlock.ITEM))
        self.blocks = blocks
        self.dummyBlock = GameBlock(0, 0, 0, 0)

    def detect(self, player, border):
        touch = {
            "right": False,
            "left": False,
            "bottom": False,
            "top": False,
            "hasEvent": False
        }

        for block in self.blocks:
            if block.clipline(player.x + player.w - 1 + border, player.y, player.x + player.w - 1 + border,
                              player.y + player.h - 1):
                touch = checkBlock(touch, "left", block)
            if block.clipline(player.x + player.w - 1, player.y + player.h - 1 + border, player.x,
                              player.y + player.h - 1 + border):
                touch = checkBlock(touch, "bottom", block)
            if block.clipline(player.x - border, player.y, player.x - border, player.y + player.h - 1):
                touch = checkBlock(touch, "left", block)
            if block.clipline(player.x, player.y - border, player.x + player.w - 1, player.y - border):
                touch = checkBlock(touch, "top", block)

        return touch
