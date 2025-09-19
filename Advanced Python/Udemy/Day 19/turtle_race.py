import turtle
from turtle import Turtle, Screen
import random
"""
This handles events, screen listeners
"""

screen = Screen()
"""
This set the screen size
"""
is_race_on = False
all_turtles = []
screen.setup(400, 400)
user_bet = screen.textinput("Make your bet?", "Which Turtle will win the race?")
print(user_bet)
colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
turtle_position = [-100,-50,0,50,100,150]
for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.goto(-220, turtle_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You lost! The {winning_turtle} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()




















