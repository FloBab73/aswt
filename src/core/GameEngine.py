class GameEngine:

    def __init__(self, gameBlocks, graphicsEngine, physicsEngine, userInput):
        self.userInput = userInput
        self.graphicsEngine = graphicsEngine
        self.gameBlocks = gameBlocks
        self.physicsEngine = physicsEngine

    def run(self):
        key = self.userInput.getUserInput()
        events = self.physicsEngine.movement(key)

        if len(events) > 0:
            if events["type"] == "item":
                self.gameBlocks.remove(events["block"])

        self.graphicsEngine.draw()
