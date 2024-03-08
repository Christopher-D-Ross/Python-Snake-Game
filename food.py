import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # Creating a 10 X 10 circle.
        self.color("black")
        self.speed("fastest")  # Speeding up the transition of the food disappearing then being created again.
        # For a 600 X 600 screen the x and y-axis will be -300 to 300.
        # -280 and 280 are chosen to prevent the circle from being right on the wall.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
