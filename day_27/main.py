import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tk.Entry(width=10)
input.pack()

window.mainloop()
