from tkinter import *

FONT = ("Arial", 14, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=15)
entry.insert(END, string="0")
entry.grid(column=1,row=0)

# Label
miles_label = Label(text="Miles", font=FONT)
# to place in the center of the screen
miles_label.grid(column=2, row=0)

# Label
km_result_label = Label(text="0", font=FONT)
# to place in the center of the screen
km_result_label.grid(column=1, row=1)

# Label
km_label = Label(text="Km", font=FONT)
# to place in the center of the screen
km_label.grid(column=2, row=1)

# Label
is_equal_label = Label(text="is equal to", font=FONT)
# to place in the center of the screen
is_equal_label.grid(column=0, row=1)

def button_clicked():
    miles = entry.get()
    km_result_label.config(text=round(float(miles) * 1.60934))

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)


window.mainloop()