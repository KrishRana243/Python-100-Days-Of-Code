#U.S. States Game
#Type Exit to end Game

import turtle
import pandas

screen = turtle.Screen()

image = "./Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

file = "./Day25/50_states.csv"
data = pandas.read_csv(file)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another states name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Day25/States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

screen.exitonclick()

