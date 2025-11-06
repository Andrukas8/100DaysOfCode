import tkinter as tk

COEF = 1.60934

FONT = ("Arial", 12, "normal")


def calculate():
    miles = input.get()
    km = round(float(miles) * COEF, 2)
    result_lbl.config(text=f"{km}")


window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=100)

is_equal_to_lbl = tk.Label(text="is equal to", font=FONT)
is_equal_to_lbl.grid(column=0, row=1)

result_lbl = tk.Label(text="0", font=FONT)
result_lbl.grid(column=1, row=1)

km_lbl = tk.Label(text="Km", font=FONT)
km_lbl.grid(column=2, row=1)

calc_btn = tk.Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)

input = tk.Entry()
input.grid(column=1, row=0)

miles_lbl = tk.Label(text="Miles", font=FONT)
miles_lbl.grid(column=2, row=0)

window.mainloop()
