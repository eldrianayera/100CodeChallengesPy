import turtle
from turtle import Turtle , Screen
import random


t = Turtle()
screen = Screen()

t.color('cyan3')
t.shape('turtle')
colors = ['lavender', 'peachpuff', 'lightcoral', 'mintcream', 'powderblue', 'rosybrown', 'honeydew', 'thistle', 'seashell', 'lightsteelblue']
dark_aesthetic_colors = ['slateblue', 'darkolivegreen', 'midnightblue', 'sienna', 'teal', 'indigo', 'darkslategray', 'maroon', 'darkorchid', 'darkgoldenrod']


def draw_sides(sides) :
    angle = 360 / sides
    for side in range(sides) :
        t.forward(100)
        t.right(angle)

for shape_side in range(3,11) :
    t.color(random.choice(dark_aesthetic_colors))
    draw_sides(shape_side)