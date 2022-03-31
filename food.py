from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        random_x = random.randint(-300,300)
        random_y = random.randint(-300,300)
        self.goto(random_x,random_y)