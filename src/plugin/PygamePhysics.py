from src.core.PhysicsEngine import PhysicsEngine


class PygamePhysics(PhysicsEngine):

    def __init__(self, collisionDetection, activeBlocks):
        super().__init__(collisionDetection, activeBlocks)

    # moves player one pixel at a time to stop at the right moment
    def move(self, index, distance_x, distance_y):
        x = 0
        y = 0
        event = []
        if distance_x < 0:
            x = -1
            distance_x = abs(distance_x)
        elif distance_x > 0:
            x = 1
        if distance_y < 0:
            y = -1
            distance_y = abs(distance_y)
        elif distance_y > 0:
            y = 1

        go_x = True
        go_y = True
        while go_x or go_y:
            if distance_x > 0:
                distance_x -= 1
            else:
                x = 0
                go_x = False
            if distance_y > 0:
                distance_y -= 1
            else:
                y = 0
                go_y = False

            self.activeBlocks[index].moveBlock(x, y)

            touch = self.collisionDetection.detect(0, 1)

            if touch["hasEvent"]:
                event = touch["event"]
            if touch["bottom"] or touch["top"]:
                y = 0
            if touch["left"] or touch["right"]:
                x = 0

        return event

    # checks for button input and calculates movement
    def movement(self, key):
        touch = self.collisionDetection.detect(0, 1)

        if touch["bottom"]:
            self.velocity_y = 0
        elif touch["top"]:
            self.velocity_y = self.gravity
        else:
            self.velocity_y += self.gravity

        if touch["left"]:
            if self.velocity_x < 0:
                self.velocity_x = 0
        else:
            if key["left"]:
                if self.velocity_x >= -self.maxSpeed:
                    self.velocity_x -= self.acceleration
            else:
                if self.velocity_x < 0:
                    self.velocity_x += self.deceleration

        if touch["right"]:
            if self.velocity_x > 0:
                self.velocity_x = 0
        else:
            if key["right"]:
                if self.velocity_x <= self.maxSpeed:
                    self.velocity_x += self.acceleration
            else:
                if self.velocity_x > 0:
                    self.velocity_x -= self.deceleration

        if key["up"] and touch["bottom"]:
            self.velocity_y = -9

        event = self.move(0, self.velocity_x, self.velocity_y)
        return event
