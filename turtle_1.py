import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

t = turtle.Turtle()
t.speed(0.1)


for color in range(250):
	t.pencolor(random.choice(colors))
	t.fd(color)
	t.lt(54)
