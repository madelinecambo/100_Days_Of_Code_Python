from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #

PURPLE = '#b8b7fd'
PINK = '#ffc8dd'
DARK_PINK = '#ffafcc'
BLUE = '#b8ceff'
GREEN = '#CEE9b3'

FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_title.config(text="Timer", fg=BLUE, font=(FONT_NAME, 35, "bold"), bg=PINK)
    check_marks.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        timer_title.config(text="Long Break", fg=BLUE, font=(FONT_NAME, 35, "bold"), bg=PINK)
        countdown(long_break_sec)
    #If it's the 2nd, 4th, 6th, rep:
    elif reps % 2 == 0:
        timer_title.config(text="Short Break", fg=BLUE, font=(FONT_NAME, 35, "bold"), bg=PINK)
        countdown(short_break_sec)
    else:
        timer_title.config(text="Work", fg=PURPLE, font=(FONT_NAME, 35, "bold"), bg=PINK)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=PINK)

#Timer Labels
timer_title = Label(text="Timer", fg=BLUE, font=(FONT_NAME, 35, "bold"), bg=PINK)
timer_title.grid(column=1, row=0)

# Create Canvas
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

#Check Marks
check_marks = Label(text="", fg=PURPLE, font=(FONT_NAME, 15, "bold"), bg=PINK)
check_marks.grid(column=1, row=3)


window.mainloop()