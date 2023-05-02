from src.application.CollisionDetection import Direction


class BlockMover:
    def __init__(self, collision_detection):
        self.collision_detection = collision_detection

    def move_block(self, subject, objects, distance_x, distance_y):
        x = 0
        y = 0
        go_x = True
        go_y = True
        direction_x = 0
        direction_y = 0

        if distance_x < 0:
            direction_x = -1
        elif distance_x > 0:
            direction_x = 1
        else:
            go_x = False

        if distance_y < 0:
            direction_y = -1
        elif distance_y > 0:
            direction_y = 1
        else:
            go_y = False

        while go_x or go_y:
            touch = self.collision_detection.detect(subject, objects, abs(distance_x), abs(distance_y))

            if Direction.RIGHT not in touch and direction_x == 1 or Direction.LEFT not in touch and direction_x == -1:
                x = distance_x
                go_x = False
            else:
                if distance_x != 0:
                    distance_x -= direction_x
                else:
                    go_x = False

            if Direction.BOTTOM not in touch and direction_y == 1 or Direction.TOP not in touch and direction_y == -1:
                y = distance_y
                go_y = False
            else:
                if distance_y != 0:
                    distance_y -= direction_y
                else:
                    go_y = False

        subject.move(x, y)
