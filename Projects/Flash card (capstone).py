from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("C:\\Users\\Asus\\Downloads\\Untitled spreadsheet - Sheet1 (1).csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["ENGLISH WORDS"])
    canvas.itemconfig(card_title, text="ENGLISH WORDS", fill="black")
    canvas.itemconfig(card_word, text=current_card["ENGLISH WORDS"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="MEANING")
    canvas.itemconfig(card_word, text=current_card["MEANING"])
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words to learn.csv")
    next_card()


window = Tk()
window.title("FLASH GAME")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="C:\\Users\\Asus\\Pictures\\card_front1.png")
back_image = PhotoImage(file="C:\\Users\\Asus\\Pictures\\card_back1.png")
card_background=canvas.create_image(400, 263,image=front_image)
card_title=canvas.create_text(400, 150,text="", font=("Ariel",40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="C:\\Users\\Asus\\Pictures\\wrong1.png")
incorrect_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
incorrect_button.grid(row=1,column=0)
right_image = PhotoImage(file="C:\\Users\\Asus\\Pictures\\right1.png")
corrct_button = Button(image=right_image, highlightthickness=0, command=is_known)
corrct_button.grid(row=1, column=1)
next_card()

# TODO FLIP THE CARD

















window.mainloop()
