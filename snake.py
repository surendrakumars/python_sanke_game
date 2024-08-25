from turtle import Turtle, Screen
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.count = 0
        self.segments = []
        for i in range(1, 4):
            self.add_segment(self.count)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head = self.segments[0]
        self.head.forward(20)

    def add_segment(self,count):
        jim = Turtle()
        jim.shape("square")
        jim.color("white")
        jim.penup()
        jim.goto(x=self.count, y=0)
        self.count -= 20
        self.segments.append(jim)

    def extend(self):
        self.add_segment(self.segments[-1].pos())
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




