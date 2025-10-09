from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
is_equal_to = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to.grid(row=1, column=0)

miles_text = Label(text="Miles", font=("Arial", 24, "bold"))
miles_text.grid(row=0, column=2)

km_text = Label(text="Km", font=("Arial", 24, "bold"))
km_text.grid(row=1, column=2)

km = Label(text="0", font=("Arial", 24, "bold"))
km.grid(row=1, column=1)

# Input Box
input = Entry(width=8)
input.grid(row=0, column=1)

def button_clicked():
    intput = int(input.get())
    # Distance covered in km = (n x 1.609344) kilometers
    answer = round(intput * 1.609344, 2)
    km.config(text=answer)


# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(row=1, column=1)
#
# button1 = Button(text="Click Me", command=button_clicked)
# button1.grid(row=1, column=1)
#
# button2 = Button(text="Click Me", command=button_clicked)
# button2.grid(row=0, column=2)
#
# input = Entry(width=10)
# input.grid(row=3, column=3)

window.mainloop()
