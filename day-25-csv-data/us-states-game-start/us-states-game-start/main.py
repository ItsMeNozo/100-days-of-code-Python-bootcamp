import turtle
import pandas

# ref: https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []  # to print all missing states later
data = pandas.read_csv("50_states.csv")

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 U.S States Correct", "What's another state name?")
    state_line = data[data.state.str.lower() == answer_state.lower()]

    if answer_state.lower() == "exit":
        states_not_guessed = [state for state in data.state if state not in guessed_states]
        not_guessed_state_dataFrame = pandas.DataFrame({"states": states_not_guessed})
        not_guessed_state_dataFrame.to_csv("states_to_learn.csv")
        break
    if state_line.empty:
        continue
    state = state_line.state.item()  # Item return the first element
    if state in guessed_states:
        continue
    guessed_states.append(state)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(int(state_line.x), int(state_line.y))
    t.write(state)

