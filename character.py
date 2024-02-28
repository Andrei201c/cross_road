from turtle import Turtle

STEP = 5
POSITION = (0, -230)

class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.9)
        self.penup()
        self.setheading(90)
        self.goto(POSITION)
        self.color('red')
        self.fillcolor('darkred')

    def movement(self):
        self.forward(STEP)

    def reset(self):
        self.goto(POSITION)


