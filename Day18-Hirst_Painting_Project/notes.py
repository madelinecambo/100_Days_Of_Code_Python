# from turtle import Turtle, Screen, forward, left

#aliasing modules
import turtle as t
import random

# Not best practices
# from turtle import *
# from random import *

# very confusing, and hard to tell where the functions are coming from.

tim = t.Turtle()
tim.shape("turtle")
tim.color("DeepPink")

# for _ in range(0,4):
#     tim.forward(100)
#     tim.left(90)


# Challenge 2: Draw dashed line. 10 paces line, 10 paces no line, Repeat 50x

# for _ in range(0, 15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge #3: Draw a triangle, square, pentagon, hexagon, heptagon, ocatogon, nonagon and decagon
# each side is 100 in length
# random color for each shape

colors = ['DarkOrchid', 'DeepPink', 'DeepSkyBlue', 'aquamarine', 'LightPink',
          'LightGreen', 'LightCoral', 'plum', 'lavender', 'cornflowerblue']

directions = [0, 90, 180, 270]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for side in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     tim.width(3)
#     tim.speed(0)
#     draw_shape(shape_side_n)

# Challenge #4: Draw a Random Walk
# random movements, north, east, south or west
# same distance, but different directions
# increase the thickness of the lines, speed up the turtle so it draws faster.

# for step in range(0, 100):
#     tim.color(random.choice(colors))
#     tim.width(3)
#     tim.speed(0)
#     tim.setheading(random.choice(directions))
#     tim.forward(50)


# Challenge #5 - select random colors using a python tuple
# tuples are immutable. They cannot be changed
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# for step in range(0, 100):
#     selected_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.color(random_color())
#     tim.width(3)
#     tim.speed(0)
#     tim.setheading(random.choice(directions))
#     tim.forward(50)

# Challenge #6: Draw a Spirograph
# draw a circle, title the circle. Continue drawing circles

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()



