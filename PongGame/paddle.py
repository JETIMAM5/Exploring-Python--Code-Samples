from turtle import Turtle
from ball import Ball

ball = Ball()
ball.hideturtle()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.movement = 20

    def go_up(self):
        new_y = self.ycor() + self.movement
        self.goto(self.xcor(), new_y)
        if ball.bounce_x():
            self.movement += 20

    def go_down(self):
        new_y = self.ycor() - self.movement
        self.goto(self.xcor(), new_y)
        if ball.bounce_x():
            self.movement -= 20
