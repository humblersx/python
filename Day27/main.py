from tkinter import *

window = Tk()
window.title("My First Tk Window")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)



def button_clicked():
    textinput = input.get()
    my_label.config(text=textinput)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(row=1, column=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=3, column=3)



window.mainloop()


# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)
