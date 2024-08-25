from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        pos_food_x = random.randint(-280, 280)
        pos_food_y = random.randint(-280,280)
        self.goto(pos_food_x,pos_food_y)
    def refresh(self):
        pos_food_x = random.randint(-280, 280)
        pos_food_y = random.randint(-280, 280)
        self.goto(pos_food_x,pos_food_y)