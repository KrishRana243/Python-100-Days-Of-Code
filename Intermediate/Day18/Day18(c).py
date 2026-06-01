import turtle
import random

venusaur = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
venusaur.pensize(15)
venusaur.speed("fastest")

for _ in range(200):
    venusaur.color(random_color())
    venusaur.forward(30)
    venusaur.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()