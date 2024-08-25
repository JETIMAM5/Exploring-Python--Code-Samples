from turtle import Turtle
ORIGIN = (0, 0)
WIDTH = 800
HEIGHT = 600


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(ORIGIN)
        self.speed('normal')

    def ball_move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
