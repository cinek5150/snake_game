from turtle import Turtle
ALIGMNENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Your score: {self.score}", align=ALIGMNENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def loose_message(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGMNENT, font=FONT)
