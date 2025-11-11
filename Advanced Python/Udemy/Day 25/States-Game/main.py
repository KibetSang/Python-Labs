import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
guesses_remaining = 50
guessed_states = []
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
while game_on:
    if guesses_remaining < 0:
        game_on = False
    answer_state = screen.textinput(title=f"Guess the State, {guesses_remaining}/50",
                                    prompt="What is your guess?").title()
    if answer_state == "Exit":
        break
        game_on = False
        guesses_remaining -= 1
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        guesses_remaining -= 1
    else:
        guesses_remaining -= 1
# Check in the answer is one of the 50 states
# I if they got it right the turtle should move to x y locationa and
# Write the name of the state
not_guessed_states = []
for state in all_states:
    if state not in guessed_states:
        not_guessed_states.append(state)
df = pd.DataFrame(not_guessed_states)
df.to_csv('guessed_state.csv')
