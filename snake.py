from turtle import Turtle

s_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in s_pos:
            self.add_segment(i)

    def add_segment(self,i):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(i)
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].pos())

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]


    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
