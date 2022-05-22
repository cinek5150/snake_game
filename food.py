from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(0.5)
        self.speed("fastest")
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
