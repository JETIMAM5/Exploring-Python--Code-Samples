import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
misses = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct",
                                    prompt="What's the another state's name?").title()

    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                misses.append(state)
                missed_states = pd.Series(misses)
                missed_states.to_csv("missed_states.csv", index=False)
        break
    if answer_state in states:
        game_turtle = turtle.Turtle()
        game_turtle.hideturtle()
        game_turtle.penup()
        state_data = data[data.state == answer_state]
        game_turtle.goto(state_data.x.item(), state_data.y.item())
        game_turtle.write(answer_state, align="center")
        guessed_states.append(answer_state)
