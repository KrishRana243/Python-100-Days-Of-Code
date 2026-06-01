from turtle import Turtle, Screen
import random

venusaur = Turtle()

colors = ["darkblue","limegreen","darkviolet","gold","brown",
          "indianred","deepskyblue","wheat","slategrey","aquamarine",
          "darkorchid","seagreen","pink","black"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        venusaur.forward(100)
        venusaur.right(angle)

for shape_side in range(3,11):
    venusaur.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()