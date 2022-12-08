from tkinter import *

FONT = ("Arial", 11)


def calculate():
    if input_miles.get() != "":
        km = "%.2f" % (int(input_miles.get()) * 1.609)  # km is a str because of %f formatter
        km_result_label.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=10)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)
miles_label.config(padx=5)
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)
km_result_label = Label(text="0", font=FONT)
km_result_label.grid(row=1, column=1)


input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

button_calculate = Button(text="Calculate", command=calculate, font=FONT)
button_calculate.grid(row=2, column=1)

window.mainloop()


