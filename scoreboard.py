from turtle import Turtle
FONT = ("Courier", 18, "normal")
SPEED = .5


class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.high_score = Turtle()
        self.high_score.penup()
        self.high_score.hideturtle()
        self.high_score.color("white")
        self.high_score.goto(220, 260)
        self.high_score.hiscore = 0
        self.goto(-250,260)
        # self.highscore = 0
        self.score = 0
        self.speed = SPEED
        self.update()
        self.update_highscore()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def update_highscore(self):
        self.high_score.clear()
        self.write(f"Score: {self.high_score.hiscore}", font=FONT)

    def increase_highscore(self):
        high_score = Turtle()
        high_score.color("white")
        high_score.goto(220, 260)
        if self.score > self.hig_score.hiscore:
            high_score = self.score
            self.highscore = high_score
        self.update_highscore()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", font=FONT)

    def increase_speed(self):
        self.speed /= 3

    def restart(self):
        self.score = 0
