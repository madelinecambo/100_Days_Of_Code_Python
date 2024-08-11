PINK = '#ffc8dd'
FONT = ("Arial", 10, "bold")
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)


    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(END, password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    username = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0 or len(username) == 0:
        messagebox.showinfo("Opps", "Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open('data.json', 'w') as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=PINK)

# Create Canvas
canvas = Canvas(width=200, height=200, bg=PINK, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=PINK)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=PINK)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=PINK)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()
username_entry = Entry(width=30)
username_entry.grid(column=1, row=2)
username_entry.insert(END, "madelineann11@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password, width=20)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", command=save, width=30)
add_button.grid(column=1, row=4, columnspan=2)


def find_password():
    # try to load json
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    try:
        entry = data[website_entry.get()]
    except KeyError:
        messagebox.showinfo("Error", f"No details for {website_entry.get()} exists")

    else:
        email = entry['email']
        password = entry['password']
        messagebox.showinfo(f"{website_entry.get()}", f"Email: {email}\nPassword: {password}")

# Search Button
search_button = Button(text="Search", command=find_password, width=20)
search_button.grid(column=2, row=1)





window.mainloop()