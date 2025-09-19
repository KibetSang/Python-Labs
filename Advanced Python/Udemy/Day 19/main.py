from turtle import Turtle, Screen

"""
This handles events, screen listeners
"""
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(100)
def move_backward():
    tim.backward(100)
def counter_clockwise():
    tim.left(120)
def clockwise():
    tim.right(120)
def clear_drawing():
    tim.clear()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "space")
screen.onkey(clear_drawing, "c")


screen.exitonclick()




















