class PhysicsEngine:
    gravity = 1
    acceleration = 1
    deceleration = 1
    maxSpeed = 2

    def __init__(self, collision_detection):
        self.collision_detection = collision_detection

    def movement(self, subject, objects, velocity_x, velocity_y):
        pass
