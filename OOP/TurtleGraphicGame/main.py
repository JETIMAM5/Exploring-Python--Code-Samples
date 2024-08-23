import turtle as t
from turtle import Screen as s
import random

t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim = t.Turtle()
# Drawing a square :
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# Dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Polygons


# def draw_shape(num_sides):
#     for i in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for corner in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(corner)


# Random Moving
#
# Directions = [0, 90, 180, 270, 360]
#
# tim.pensize(15)
# tim.speed("fastest")
#
# for i in range(360):
#     tim.setheading(random.choice(Directions))
#     tim.pencolor(random_color())
#     tim.pendown()
#     tim.forward(30)

# Circles and Spirograph
tim.speed("fastest")


def draw_spirograph(size_of_gap):

    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen = s()
screen.exitonclick()




