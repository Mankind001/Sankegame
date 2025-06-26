from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y, value):
        super().__init__()
        self.clear()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.score = value
        self.highscore=0
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"score: {self.score} highscore:{self.highscore}", align="center", font=("Courier", 24, "bold"))

    def increase(self):
        self.score += 1
        self.write_score()

    def highscore_update(self):
        self.highscore=self.score
        self.score=0
        self.write_score()




