from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.05
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_marks_label.config(text='')
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long break', fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(REPS/2)):
            marks += '✓'
        if REPS % 2 == 0:
            check_marks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title('Pomodoro')
window.config(padx=25, pady=25, bg=YELLOW)


canvas = Canvas(width=240, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(120, 112, image=tomato_img)
timer_text = canvas.create_text(120, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# "Timer" label
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(row=0, column=1)


# 'Start' button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


# 'Reset' button
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


# Check mark label
check_marks_label = Label(fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=2, column=1)


window.mainloop()
