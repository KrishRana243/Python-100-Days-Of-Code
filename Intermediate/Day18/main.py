#Hirst Spot Painting Project
import colorgram 

rgb_colors = []
colors = colorgram.extract("./Day18/bubble.png",30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_list = rgb_colors
print(rgb_colors)

import turtle
import random

turtle.colormode(255)
venusaur = turtle.Turtle()
venusaur.speed("fastest")
venusaur.penup()
venusaur.hideturtle()

venusaur.setheading(225)
venusaur.forward(300)
venusaur.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots + 1):
    venusaur.dot(20, random.choice(color_list))
    venusaur.forward(50)

    if dot_count % 10 == 0:
        venusaur.setheading(90)
        venusaur.forward(50)
        venusaur.setheading(180)
        venusaur.forward(500)
        venusaur.setheading(0)

screen = turtle.Screen()
screen.exitonclick()