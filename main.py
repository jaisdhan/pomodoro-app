from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
check=""
def count_down(count):
    global check
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        sec = count_sec
        count_sec = "0"+ str(sec)

    if count_min < 10:
        min = count_min
        count_min = "0"+ str(min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2:
            check+="✔"
            check_mark.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




title =Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)



start_button=Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button=Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg="lawngreen", bg=YELLOW, font=(FONT_NAME,14,"bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
