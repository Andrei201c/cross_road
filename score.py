from turtle import Turtle

ALIGN = 'center'
FONT = ("Verdana", 20, 'bold')


class  Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color('yellow')
        self.penup()
        self.goto(-300, 200)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"LEVEL: {self.score}", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align=ALIGN, font=FONT)
