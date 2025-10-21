from tkinter import Tk, Canvas, PhotoImage

from tkmacosx import Button
import pandas
import random


# Global vars
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient='records')
random_word = random.randint(0, 100)
french_word = data_dict[random_word]["French"]
english_word = data_dict[random_word]["English"]
length = 100

def get_newword():
    global data_dict, french_word, english_word, length, random_word
    random_word = random.randint(0, length)
    print(f"Random Word: {random_word}")
    french_word = data_dict[random_word]["French"]
    english_word = data_dict[random_word]["English"]



def gen_wordpair():
    # Code to pull french words into pandas df
    global data_dict, fw_text, flip_timer

    window.after_cancel(flip_timer)

    # Clear previous text before setting new one
    canvas.itemconfig(fw_text, text="")


    # call to get new word pair
    get_newword()

    # Now display french word on card
    canvas.itemconfig(fw_text, text=french_word, fill="black", font=FONT2)
    canvas.grid(row=0, column=0, columnspan=2)

    canvas.itemconfig(canvas_image, image=card_front_img)

    canvas.itemconfig(french_text, text="French", fill="black", font=FONT1)

    flip_timer = window.after(3000, func=flip_word)

def gen_wordpair_right():
    global data_dict, random_word, data, length
    if length > 0:
        data_dict.pop(random_word)
        data = pandas.DataFrame(data_dict)
        data.to_csv("data/words_to_learn.csv", index=False)
        data = pandas.read_csv("data/words_to_learn.csv")
        data_dict = data.to_dict(orient='records')
        length -= 1
        gen_wordpair()
    else:
        exit()

def gen_wordpair_wrong():

    gen_wordpair()

# Run when 3 seconds are up and card flips
def flip_word():
    # Code to pull french words into pandas df
    global data_dict, fw_text, english_word


    # Change to card back background
    canvas.itemconfig(canvas_image, image=card_back_img)

    # Change to English
    canvas.itemconfig(french_text, text="English", fill="white", font=FONT1)

    canvas.itemconfig(fw_text, text=english_word, fill="white", font=FONT2)
    canvas.grid(row=0, column=0, columnspan=2)


BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

french_text = canvas.create_text(400, 150, text="French", fill="black", font=FONT1)
fw_text = canvas.create_text(400, 263, text="French", fill="black", font=FONT2)
#ew_text = canvas.create_text(400, 263, text="English", fill="black", font=FONT2)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, borderless=1, bg=BACKGROUND_COLOR, width=130, command=gen_wordpair_wrong)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, borderless=1, bg=BACKGROUND_COLOR, width=130, command=gen_wordpair_right)
right_button.grid(row=1, column=1)



gen_wordpair()



window.mainloop()