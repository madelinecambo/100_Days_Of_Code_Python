from tkinter import *
from quiz_brain import QuizBrain
from textwrap import wrap

THEME_COLOR = "#375362"
FONT_WORD = ("Ariel", 20, "italic")
FONT_SCORE = ("Ariel", 15, "bold")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",
                                 font=FONT_SCORE,
                                 fg="white",
                                 bg=THEME_COLOR,
                                 padx=20,
                                 pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Question Text",
                                                     fill="black",
                                                     font=FONT_WORD,
                                                     width=280)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Add True and False Button Images
        self.false_image = PhotoImage(file='images/false.png')
        self.true_image = PhotoImage(file='images/true.png')

       # Buttons
        self.false_button = Button(image=self.false_image,
                                   highlightthickness=0,
                                   command = self.false_button_pressed)
        self.false_button.grid(row=2, column=1)
        self.true_button = Button(image=self.true_image,
                                  highlightthickness=0,
                                  command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)

        self.show_next_question()
        self.window.mainloop()

    def show_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def false_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.show_next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")







