from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_add = 6
        self.y_add = 7.5
        self.move_timedelay = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_add, self.ycor() + self.y_add)

    def bounce_top_bottom(self):
        self.y_add *= -1

    def bounce_sides(self):
        self.x_add *= -1
        self.move_timedelay *= 0.9

    def set_x_add(self, n):
        self.x_add = n

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_sides() # bounce in opposite direction
        self.move_timedelay = 0.1