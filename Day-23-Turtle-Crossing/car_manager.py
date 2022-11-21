from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUMBER_OF_CARS = 25


class CarManager:
    def __init__(self):
        self.car_list = []
        self.generate_cars()
        self.speed = MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(random.randint(-300, 300), random.randint(-250, 250))
        self.car_list.append(new_car)

    def generate_cars(self):
        for _ in range(NUMBER_OF_CARS):
            self.create_car()

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.speed)
            if car.xcor() < -380:
                car.goto(300, car.ycor())
                car.color(random.choice(COLORS))

    def increase_speed(self):
        self.speed += 5
