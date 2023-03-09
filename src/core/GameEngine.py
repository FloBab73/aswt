class GameEngine:

    def __init__(self, game_blocks, graphics_engine, player, user_input):
        self.player = player
        self.userInput = user_input
        self.graphicsEngine = graphics_engine
        self.gameBlocks = game_blocks

    def run(self):
        key = self.userInput.get_user_input()

        self.player.movement(key)

        self.graphicsEngine.draw()

    def remove_block(self, x, y):
        for block in self.gameBlocks:
            if block.position().x == x and block.position().y == y:
                self.gameBlocks.remove(block)
