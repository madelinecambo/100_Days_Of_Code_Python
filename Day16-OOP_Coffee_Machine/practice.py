# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color("deeppink")
# timmy.shape("turtle")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Changing attributes to update the styling of our table.
print(table.align)
table.align = 'l'
print(table)


