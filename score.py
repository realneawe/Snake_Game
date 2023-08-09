from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
END_FONT = ("Arial", 25, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score_data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 320)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 320)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_edge(self):
        time.sleep(0.0001)
        self.color("white")
        self.pensize(20)
        self.penup()
        self.goto(300, 300)
        self.pendown()
        self.goto(300, -300)
        self.goto(-300, -300)
        self.goto(-300, 300)
        self.goto(300, 300)
        self.penup()