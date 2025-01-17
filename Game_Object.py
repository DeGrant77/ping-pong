from Ball_movement import Point
from Ball_movement import Velocity
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5


class Ball:
    """
    The Ball class makes use of the Point and Velocity classes to determine its properties and behaviours
    """

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()

    def draw(self):  # draws the ball at a random location
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.WHITE, 45)

    def advance(self):  # moves the ball in time
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_vertical(self):  # prevents ball from moving off-screen
        if self.center.y >= SCREEN_HEIGHT - BALL_RADIUS and self.velocity.dy > 0:
            self.velocity.dy *= -1

        elif self.center.y < BALL_RADIUS and self.velocity.dy < 0:
            self.velocity.dy *= -1

    def bounce_horizontal(self):  # prevents ball from moving off screen
        if self.center.x < BALL_RADIUS:
            self.velocity.dx *= -1
            self.velocity.dy *= 1

        elif self.center.x > SCREEN_WIDTH - PADDLE_WIDTH - BALL_RADIUS:
            self.velocity.dx *= -1
            self.velocity.dy *= -1

    def restart(self):  # Sets the ball at a new location when ball is lost
        if self.center.x > SCREEN_WIDTH:
            self.center.x = random.uniform(10, 20)
            self.center.y = random.uniform(50, 150)


class Paddle:
    """
    The paddle class makes use of the Point class and has methods to control the movement of the paddle
    """

    def __init__(self):
        self.center = Point()

    def draw(self):  # draws the paddle
        arcade.draw_rectangle_filled(SCREEN_WIDTH - PADDLE_WIDTH / 2, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT,
                                     arcade.color.WHITE_SMOKE)

    def move_down(self):  # allows paddle to move down without going off screen
        self.center.y -= MOVE_AMOUNT
        if self.center.y - PADDLE_HEIGHT / 2 < 0:
            self.center.y += MOVE_AMOUNT

    def move_up(self):  # allows paddle to move up without going off screen
        self.center.y += MOVE_AMOUNT
        if self.center.y + PADDLE_HEIGHT / 2 > SCREEN_HEIGHT:
            self.center.y -= MOVE_AMOUNT
