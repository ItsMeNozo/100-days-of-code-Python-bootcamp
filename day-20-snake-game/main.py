import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
turtle.resizemode("user")

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
turtles = []


def init_turtle(x, y):
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.setposition(x, y)
    return t


for i in range(3):
    turtles.append(init_turtle(starting_pos[i][0], starting_pos[i][1]))

screen.exitonclick()
