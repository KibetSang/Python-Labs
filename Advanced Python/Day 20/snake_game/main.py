from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


screen.exitonclick()