import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")


def get_user_answer():
    return screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                            prompt="What's another state's name?").title()


image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = get_user_answer()

    if answer_state == "Exit":
        break
    elif answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(state_data["state"].item())
        guessed_states.append(state_data["state"].item())
    else:
        answer_state = get_user_answer()

# Generate states_to_learn.csv
states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)


pd.Series(states_to_learn).to_csv("states_to_learn.csv")
