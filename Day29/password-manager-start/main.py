from tkinter import Tk, Canvas, Label, PhotoImage, Entry
from tkinter import messagebox
from tkmacosx import Button
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():

    web_input = website_entry.get().lower()
    if web_input == "" :
        messagebox.showinfo(title="Empty fields", message="Please don't leave Website field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="No JSON", message="No Data File Found")

        try:
            messagebox.showinfo(title="Find Password", message=f"Website: {web_input}\n"
                                f"Email: {data[web_input]["email"]}\n"
                                f"Password: {data[web_input]["password"]}")
        except KeyError:
            messagebox.showinfo(title="No Website", message="No details for the website exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Take inputs from entries and button is clicked, save data into a file (data.txt)
# Website | Username | Password

def save():
    web_input = website_entry.get().lower()
    username_input = username_entry.get().lower()
    password_input = password_entry.get()
    new_data = {
        web_input: {
            "email": username_input,
            "password": password_input
        }
    }

    if web_input != "" and password_input != "":
        # is_ok = messagebox.askokcancel(title=web_input, message=f"These are the details entered: \nWebsite: {web_input}"
        #                                                 f"\nUsername: {username_input} "
        #                                                 f"\nPassword: {password_input} \nIs it ok to save?")

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
                data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)



        website_entry.delete(0, 'end')
        username_entry.delete(0, 'end')
        username_entry.insert(0, "humblers@gmail.com")
        password_entry.delete(0, 'end')

    else:
        messagebox.showinfo(title="Empty fields", message="Please don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #

WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Arial"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website: ", font=(FONT_NAME, 20), bg=WHITE, fg=BLACK, highlightthickness=0)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username: ", font=(FONT_NAME, 20), bg=WHITE, fg=BLACK, highlightthickness=0)
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=(FONT_NAME, 20), bg=WHITE, fg=BLACK, highlightthickness=0)
password_label.grid(row=3, column=0)

# Entry

website_entry = Entry(width=19, bg=WHITE, fg="black")
website_entry.focus()
website_entry.grid(row=1, column=1, sticky='w')


username_entry = Entry(width=35, bg=WHITE, fg="black")
username_entry.insert(0, "humblers@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky='w')


password_entry = Entry(width=19, bg=WHITE, fg="black")
password_entry.grid(row=3, column=1, sticky='w')

# Buttons

genpass_button = Button(text="Generate Password", borderless=1, width=130, command=generate_password)
genpass_button.grid(row=3, column=2, sticky='w')

search_button = Button(text="Search", borderless=1, width=130, command=find_password)
search_button.grid(row=1, column=2, sticky='w')

add_button = Button(text="Add", borderless=1, width=332, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()

