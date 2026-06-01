import turtle
import random

venusaur = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

venusaur.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):        
        venusaur.color(random_color())
        venusaur.circle(100)
        venusaur.setheading(venusaur.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()