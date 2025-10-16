from tkinter import Tk, Canvas, Label, PhotoImage
from tkmacosx import Button
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
check_text = ""
otimer = None
timer_text = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer_text
    global timer

    window.after_cancel(otimer)
    # 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label = Timer
    timer.config(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, highlightthickness=0)

    # reset checkmarks
    checkmarks.config(font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN, highlightthickness=0)

    # reset reps
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    #1/3/5/7 rep
    if reps % 2 != 0:
        timer.config(text="Work", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, highlightthickness=0)
        count_down(work_sec)
    # 8th rep
    elif reps % 8 == 0:
        timer.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=RED, highlightthickness=0)
        count_down(long_break_sec)
    # 2/4/6 rep
    elif reps % 2 == 0:
        timer.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=PINK, highlightthickness=0)
        count_down(short_break_sec)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global otimer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        otimer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)





canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# Labels

timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer.grid(row=0, column=1)

checkmarks = Label(font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmarks.grid(row=3, column=1)

# Buttons

start_button = Button(text="Start", borderless=1, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", borderless=1, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()