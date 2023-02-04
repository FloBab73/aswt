class PhysicsEngine:
    velocity_x = 0
    velocity_y = 0
    gravity = 1
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, collisionDetection, activeBlocks):
        self.activeBlocks = activeBlocks
        self.collisionDetection = collisionDetection

    def move(self, index, distance_x, distance_y):
        pass

    def movement(self):
        pass
