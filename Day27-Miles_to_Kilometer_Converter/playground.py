# args - unlimited positional arguments

# the * keyword packs all the numbers into a tuple
# also accessible by index
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,4,5, 100))


# added ** in front of parameter name: now we can add unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)


# returns a dictionary of keywords and their values
calculate(2, add=3, multiply=5)

# calculate(2, add=4)


# Creating a class with optional keyword arguments
class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # works like the dictionary method, but will return none if the arguments aren't provided
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Mazda")
print(my_car.model)


# if we are going to use a lot of classes this way of importing saves typing vs import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# to place in the center of the screen
my_label.grid(column=0, row=0)

# how to configure and change (update) the properties of a component we've created
#multiple ways to update the text from the orignial text
my_label['text'] = "New Text"



#Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2,row=0)

# Entry
input = Entry(width=10)
input.grid(column=3,row=2)

#will return the input as a string
#input.get()


# must be at the end of the program. Keeps the window open


