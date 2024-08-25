from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

DEF_PADDLE_R_COORDS = (350, 0)
DEF_PADDLE_L_COORDS = (-350, 0)
TOP_BOUNCING_COORD = 280
BOTTOM_BOUNCING_COORD = -280

r_paddle = Paddle(DEF_PADDLE_R_COORDS)
l_paddle = Paddle(DEF_PADDLE_L_COORDS)
ball = Ball()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collusion with the walls (top and the bottom)
    if ball.ycor() > TOP_BOUNCING_COORD or ball.ycor() < BOTTOM_BOUNCING_COORD:
        ball.bounce_y()

    # Detect collusion with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
