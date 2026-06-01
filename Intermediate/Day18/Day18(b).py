from turtle import Turtle, Screen
import random

venusaur = Turtle()

colors = ["darkblue","limegreen","darkviolet","gold","brown",
          "indianred","deepskyblue","wheat","slategrey","aquamarine",
          "darkorchid","seagreen","pink","black"]
directions = [0,90,180,270]
venusaur.pensize(15)
venusaur.speed("fastest")

for _ in range(200):
    venusaur.color(random.choice(colors))
    venusaur.forward(30)
    venusaur.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()