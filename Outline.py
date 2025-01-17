import arcade

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5


class Outline:
    """"
    This class is an additional and optional class to enhance the design and graphics of the game. Makes the
    background look like a real pong table!
    """

    def __init__(self):
        self.height = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH

    def draw_center_circle(self):
        arcade.draw_circle_outline(self.width / 2, self.height / 2, 50, arcade.color.WHITE, 3)

    def draw_vertical_line(self):
        arcade.draw_line(self.width / 2, 0, self.width / 2, self.height, arcade.color.WHITE, 3)

    def draw_rectangles(self):
        arcade.draw_rectangle_outline(30, self.height / 2, 100, 100, arcade.color.WHITE, 4)
        arcade.draw_rectangle_outline(380, self.height / 2, 100, 100, arcade.color.WHITE, 4)