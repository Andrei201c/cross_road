from turtle import  Screen
from character import Character
from dangers import Dangers
from score import Score
import random
import time

rand = random.randint(-240, 240)


screen = Screen()
screen.setup(800, 500)
screen.bgcolor('gray')
screen.title('CrOsS ThE RoAd')
screen.tracer(0)


character = Character()
score = Score()

screen.listen()
screen.onkeypress(character.movement, 'w')

dangers = Dangers()

keep = True

while keep:
    time.sleep(0.05)
    screen.update()

    dangers.create_car()
    dangers.move()

    for car in dangers.cars:
        if character.distance(car) < 20:
            score.game_over()
            dangers.reset()
            keep = False

    if character.ycor() == 240:
        score.increase()
        dangers.level_up()
        character.reset()

screen.exitonclick()
