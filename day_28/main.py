# Pomodoro Clock Program

import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_BUTTON = (FONT_NAME, 12, "normal")
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.configure(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.configure(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.configure(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        title_label.configure(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    mins = count // 60
    secs = count % 60

    if secs == 0:
        secs = "00"

    elif secs < 10:
        secs = f"0{secs}"

    if mins < 10:
        mins = f"0{mins}"

    timer = f"{mins}:{secs}"
    canvas.itemconfig(timer_text, text=timer)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                       font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=0)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0,
                         bg=GREEN, fg="white", font=FONT_BUTTON, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0,
                         bg=PINK, fg="white", font=FONT_BUTTON, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW,
                       font=(FONT_NAME, 15, "normal"))
check_marks.grid(column=1, row=3)

window.mainloop()
