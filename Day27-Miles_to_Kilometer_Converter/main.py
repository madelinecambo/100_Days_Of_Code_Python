import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# to place in the center of the screen
my_label.pack()














# must be at the end of the program. Keeps the window open
window.mainloop()