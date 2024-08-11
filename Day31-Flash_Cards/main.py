# BACKGROUND_COLORS = ['#75ADD0', '#9AC1E2', '#BCD2E9', '#E5E1EF', '#E0A8CD']
import random
import pandas as pd
from textwrap import wrap

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 25, "italic")
FONT_WORD = ("Ariel", 20, "bold")
from tkinter import *


current_card = {}
try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/data_science_interview_flashcards.csv")
to_learn = df.to_dict(orient="records")

#Functions
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Data Science", fill="black")
    canvas.itemconfig(card_word, text=current_card['Concept'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Answer", fill="white")
    formatted_text = '\n'.join(wrap(current_card['Answer'], 45))
    canvas.itemconfig(card_word, text=formatted_text, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def remove_card():
    to_learn.remove(current_card)
    learn_df = pd.DataFrame(to_learn)
    learn_df.to_csv("words_to_learn.csv")
    print(len(to_learn))
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


#UI Setup
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Add Flashcard Canvas with words.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 75, text="", fill="black", font=FONT_TITLE)
card_word = canvas.create_text(400, 253, text="", fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)
next_card()

# Add X and Check Buttons
unknown_image = PhotoImage(file='images/wrong.png')
known_image = PhotoImage(file='images/right.png')

unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=known_image, highlightthickness=0, command=remove_card)
known_button.grid(row=1, column=1)




window.mainloop()