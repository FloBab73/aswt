class GameEngine:

    def __init__(self, gameBlocks, graphicsEngine, player, userInput):
        self.player = player
        self.userInput = userInput
        self.graphicsEngine = graphicsEngine
        self.gameBlocks = gameBlocks

    def run(self):
        key = self.userInput.getUserInput()

        self.player.movement(key)

        self.graphicsEngine.draw()
