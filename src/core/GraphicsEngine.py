class GraphicsEngine:
    game_blocks = None

    def __init__(self, gameEngine, game_blocks, active_blocks):
        self.gameEngine = gameEngine
        self.game_blocks = game_blocks
        self.activeBlocks = active_blocks

    def draw(self):
        pass
