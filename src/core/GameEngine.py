class GameEngine:

    def __init__(self, gameBlocks, graphicsEngine, physicsEngine):
        self.graphicsEngine = graphicsEngine
        self.gameBlocks = gameBlocks
        self.physicsEngine = physicsEngine

    def run(self):

        events = self.physicsEngine.movement()

        if len(events) > 0:
            if events["type"] == "item":
                self.gameBlocks.remove(events["block"])

        self.graphicsEngine.draw()
