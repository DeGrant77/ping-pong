import random


class Point:
    """"
    This class is responsible for setting the ball at random location along the left side of the Screen.

    """

    def __init__(self):
        self.x = random.uniform(10, 20)
        self.y = random.uniform(50, 150)


class Velocity:
    """
    This class is responsible for setting a random velocity for both x and y points.
    """

    def __init__(self):
        self.dx = random.uniform(1, 2)
        self.dy = random.uniform(1, 2)


