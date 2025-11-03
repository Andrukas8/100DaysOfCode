import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label.pack(side="left")


window.mainloop()
