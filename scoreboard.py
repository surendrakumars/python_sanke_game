from turtle import Turtle

ALIGN = "center"
FONT = {"courier", 24, "normal"}


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = open("data.txt", mode="r")
        self.high_score = int(self.file.read())
        self.file.close()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align="center", font=('Arial', 10, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.file = open("data.txt", mode="w")
            self.file.write(f"{self.score}")
            self.high_score = self.score
            self.file.close()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
