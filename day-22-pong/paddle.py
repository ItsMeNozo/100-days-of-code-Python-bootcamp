from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        # default size is 20 x 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)

