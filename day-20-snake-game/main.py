from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []


def init_turtle(pos):
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    t.goto(pos)
    return t


for pos in starting_pos:
    segments.append(init_turtle(pos))
screen.update()

game_is_on = True

while game_is_on:
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

    screen.update()
    time.sleep(0.1)


screen.exitonclick()
