import tkinter as tk


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Labels
my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
button = tk.Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=0)

# Entry
input = tk.Entry(width=10)
print(input.get())
# input.pack(side="left")
input.grid(column=2, row=0)


window.mainloop()
