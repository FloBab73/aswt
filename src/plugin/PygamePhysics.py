from src.core.PhysicsEngine import PhysicsEngine


class PygamePhysics(PhysicsEngine):

    def __init__(self, collision_detection):
        super().__init__(collision_detection)

    # moves player one pixel at a time to stop at the right moment
    def move(self, subject, objects, distance_x, distance_y):
        x = 0
        y = 0
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

            subject.move(x, y)

            touch = self.collision_detection.detect(subject, objects, 1)

            if touch["bottom"] or touch["top"]:
                y = 0
            if touch["left"] or touch["right"]:
                x = 0
