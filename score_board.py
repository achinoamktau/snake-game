from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
