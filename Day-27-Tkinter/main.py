from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))  # create label;
# 2 ways to set
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()  # lay out label
my_label.grid(row=0, column=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)
# button.pack()
# Entry
input = Entry(width=10)
input.grid(row=2, column=3)

# Button 2
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(row=0, column=2)

window.mainloop()


