import turtle
import random

turtle.colormode(255)

# import colorgram
#
# extracted_colors = colorgram.extract('Image.jpg', 30)
# rgb_colors = []
# for color in extracted_colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = turtle.Turtle()
tim.penup()
tim.speed("fastest")
color_list = [(25, 107, 154), (191, 61, 25), (229, 151, 78), (219, 237, 244), (239, 212, 80), (246, 229, 237),
              (113, 176, 207), (73, 33, 12), (19, 142, 89), (148, 33, 15), (141, 53, 85), (4, 104, 70), (22, 47, 77),
              (218, 71, 90), (142, 24, 62), (229, 88, 53), (43, 46, 122), (109, 196, 152), (34, 171, 102),
              (223, 149, 14), (99, 88, 10), (213, 122, 159), (4, 95, 110), (32, 164, 194), (242, 211, 3),
              (244, 151, 176), (4, 63, 35), (245, 165, 144)]

distance = 50
dot_size = 20

x_start_position = -220
y_start_position = -150

for row in range(10):
    for col in range(10):
        color = random.choice(color_list)
        x = x_start_position + col * distance
        y = y_start_position + row * distance
        tim.goto(x, y - dot_size / 2)
        tim.dot(dot_size, color)

tim.hideturtle()
