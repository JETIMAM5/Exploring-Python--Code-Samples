from turtle import Turtle, Screen
from paddle import Paddle

DEF_PADDLE_R_COORDS = (350, 0)
DEF_PADDLE_L_COORDS = (-350, 0)

r_paddle = Paddle(DEF_PADDLE_R_COORDS)
l_paddle = Paddle(DEF_PADDLE_L_COORDS)

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
    screen.update()


screen.exitonclick()
