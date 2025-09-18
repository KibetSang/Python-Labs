# import turtle as t
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tim = Turtle()
tim.shape("arrow")
# tim.pensize(4)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# direction = [0, 90,180,270]
# tim.width(5)
# tim.speed(200)
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# tim.pencolor("RoyalBlue")
# tim.width(3)
# # Funtion to create a square
# def draw_square():
#     tim.forward(100)
#     tim.left(90)
#
# # Interate till it meets the condition

# for _ in range(15):
#     tim.pu()
#     tim.forward(2)
#     tim.pd()
#     tim.forward(2)
#     tim.pu()
#     tim.forward(2)
#     tim.pd()
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.left(angle)
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(8)


# pip install colorgram.py
import colorgram




screen = Screen()
screen.exitonclick()