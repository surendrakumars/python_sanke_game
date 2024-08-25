from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, y=270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f'score:{self.score}', align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", align= "center", font=('Arial', 20, 'normal'))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()