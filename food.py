from turtle import Turtle
from snake import Snake
import random

snake = Snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.new_pos()

    def new_pos(self):
        random_x_pos = random.randint(-245,245)
        random_y_pos = random.randint(-245,245)
        self.goto(random_x_pos,random_y_pos)

    def reset_pos(self):
        random_x_pos = random.randint(-245, 245)
        random_y_pos = random.randint(-245, 245)
        self.goto(random_x_pos,random_y_pos)

