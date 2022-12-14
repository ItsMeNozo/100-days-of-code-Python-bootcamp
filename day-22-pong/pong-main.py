from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
# Screen setup
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(x_pos=350, y_pos=0)
paddle_left = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=paddle_right.up, key="Up")
screen.onkeypress(fun=paddle_right.down, key="Down")
screen.onkeypress(fun=paddle_left.up, key="w")
screen.onkeypress(fun=paddle_left.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_timedelay)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_top_bottom()

    # detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
        ball.bounce_sides()
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_sides()

    # detect ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increment_lpoint()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increment_rpoint()


screen.exitonclick()
