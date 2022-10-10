from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Who will win the race?", prompt="Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def create_turtle(turtle_color, x, y):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_color)
    turtle.penup()
    turtle.goto(x, y)
    turtles.append(turtle)


# move to starting point
cur_y = -120
for c in colors:
    create_turtle(turtle_color=c, x=-230, y=cur_y)
    cur_y += 50

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 240:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner.")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner.")


# #Event listeners
# def forward():
#     tim.forward(10)
#
#
# def backward():
#     tim.backward(10)
#
#
# def left():
#     """turn left 10 degree"""
#     tim.setheading(tim.heading() + 10)
#
#
# def right():
#     """turn right 10 degree"""
#     tim.setheading(tim.heading() - 10)
#
#
# def clockwise():
#     tim.left(-360)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(fun=forward, key="w")
# screen.onkey(fun=backward, key="s")
# screen.onkey(fun=left, key="a")
# screen.onkey(fun=right, key="d")
# screen.onkey(fun=clear, key="c")

screen.exitonclick()
