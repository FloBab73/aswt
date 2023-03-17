class GameLoop:

    def __init__(self, game_engine, game_blocks, graphics_engine, player):
        self.game_engine = game_engine
        self.player = player
        self.graphicsEngine = graphics_engine
        self.gameBlocks = game_blocks

    def run(self):
        key = self.game_engine.get_user_input()

        self.player.movement(key)

        self.graphicsEngine.draw()

    def remove_block(self, x, y):
        for block in self.gameBlocks:
            if block.x == x and block.y == y:
                self.gameBlocks.remove(block)
