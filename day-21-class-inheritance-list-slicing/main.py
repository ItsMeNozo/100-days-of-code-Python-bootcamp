class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Breathe in, breathe out")


class Fish(Animal):
    def __init__(self):
        super().__init__() # initialize everything super class (Animal) can do

