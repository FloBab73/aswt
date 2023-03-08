class PhysicsEngine:
    gravity = 1
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, collisionDetection):
        self.collisionDetection = collisionDetection

    def movement(self, subject, objects, velocity_x, velocity_y):
        pass
