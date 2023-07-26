from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
END_FONT = ("Arial", 25, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=END_FONT)