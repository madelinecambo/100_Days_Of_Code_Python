# Import needed modules
import turtle as t
import random

# Use the colorgram package to extract colors from a photo to
# use in the Hirst painting
# import colorgram
# colors = colorgram.extract('hirst_sample.jpg', 30)

# color_tuples = []
# colors[0].rgb
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuples.append((r, g, b))
#
# print(color_tuples)

colors = [(145, 71, 106), (178, 95, 139), (124, 29, 56), (76, 17, 38), (205, 216, 237), (231, 197, 227),
          (112, 120, 170), (218, 172, 207), (83, 101, 136), (141, 94, 61), (181, 179, 222), (183, 147, 120),
          (150, 144, 64), (60, 30, 22), (194, 94, 79), (30, 33, 53), (54, 56, 91), (220, 238, 236), (116, 38, 30),
          (142, 164, 153), (228, 210, 197)]

t.colormode(255)
turtle = t.Turtle()


# Create a spot painting. 10 X 10 rows of spots.
# Each dot should be 20 in size and spaced by 50 spaces
class HirstPainting:
    def __init__(self, n_dots, spacing, dot_size, color_list):
        self.n_dots = n_dots
        self.spacing = spacing
        self.dot_size = dot_size
        self.color_list = color_list

    def get_starting_x(self):
        starting_x = (self.n_dots * self.spacing * -1) / 2
        return starting_x

    def get_starting_y(self):
        starting_y = (self.n_dots * self.spacing * -1) / 2
        return starting_y

    def get_random_color(self):
        return random.choice(self.color_list)

    def paint_row(self):
        for dot in range(self.n_dots + 1):
            turtle.dot(self.dot_size, self.get_random_color())
            turtle.forward(self.spacing)


# Use the HirstPainting class to create a painting object
painting = HirstPainting(10, 50, 20, colors)

# Initialize the settings for the start of the painting
turtle.penup()
turtle.hideturtle()
turtle.setx(painting.get_starting_x())
turtle.sety(painting.get_starting_y())
turtle.speed("slow")


# Loop through and paint the dots
for row in range(painting.n_dots):
    new_y = painting.get_starting_y() + (painting.spacing * row)
    turtle.sety(new_y)
    painting.paint_row()
    turtle.setx(painting.get_starting_x())

# Set the screen settings
screen = t.Screen()
screen.exitonclick()
