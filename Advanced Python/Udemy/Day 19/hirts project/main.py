# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random
t.colormode(255)

color_list = [(229, 228, 226), (225, 223, 224),
              (199, 175, 117), (124, 36, 24), (170, 106, 57),
              (187, 158, 51), (6, 57, 83), (205, 218, 209),
              (222, 223, 225), (108, 67, 85)]
tim = t.Turtle()

# def move_forward():
#     for _ in range(10):
#         tim.dot(7, random.choice(color_list))
#         tim.forward(20)
# for _ in range(5):
#     move_forward()
#     tim.setheading(90)
    # tim.setheading(90)
    # tim.setheading(180)
    # move_forward()
    # tim.forward(2)
    # tim.forward(10)
    # tim.setheading(180)
    # move_forward()
    # tim.right(90)
    # tim.forward(11)
    # tim.setheading(360)
for _ in range(10):
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)







screen = t.Screen()
screen.exitonclick()