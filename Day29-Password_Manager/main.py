PINK = '#ffc8dd'
FONT = ("Arial", 10, "bold")
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    print(len(password))

    if len(password) == 0 or len(website) == 0 or len(username) == 0:
        messagebox.showinfo("Opps", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {username} "
                                                     f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {username} | {password}\n")
                print('Password saved successfully')

                # After the add button is pressed. Save the information, then clear the form with the delete method
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
website_label = Label(text="Website:", font=FONT, bg=PINK)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=FONT, bg=PINK)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT, bg=PINK)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "madelineann11@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()