from faulthandler import cancel_dump_traceback_later
from pydoc import text
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
time = None
mark=""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(time)
    canvas.itemconfig(canvas_timer, text="00:00")

    global REPS
    REPS = 0
    check_label.config(text="")
    screen_label.config(text="TIMER")

    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        screen_label.config(text="WORK", fg=RED, bg=YELLOW, font=(FONT_NAME,35,"bold"))
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        screen_label.config(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        screen_label.config(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000,count_down,count-1)
    else:
        timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark,bg=YELLOW, fg=GREEN)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas_timer = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=2)


#Label
screen_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"))
screen_label.grid(column=1, row=1)

check_label = Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=7)

#buttons
start_btn = Button(text="Start",highlightthickness=0, command=timer)
start_btn.grid(column=0, row=6)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset)
reset_btn.grid(column=3, row=6)







window.mainloop()