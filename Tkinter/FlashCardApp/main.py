from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------- FUNCTIONALITIES ---------------------------- #
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict("records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(flash_card_image, image=card_front_img)
    window.after(3000, flip_card)


def flip_card():
    flash_card.itemconfig(flash_card_image, image=card_back_img)
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=current_card["English"], fill="white")


def remove_and_save():
    to_learn.remove(current_card)
    df_to_learn = pandas.DataFrame(to_learn)
    df_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------- UI SETUP -------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)
# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(window, image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=remove_and_save)
right_button.grid(row=1, column=1)
wrong_button = Button(window, image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
flash_card = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(row=0, column=0, columnspan=2)
flash_card_image = flash_card.create_image(400, 263, image=card_front_img)
card_title = flash_card.create_text(400, 150, text="Flash Card", font=("Arial", 40, "italic"))
card_word = flash_card.create_text(400, 263, text="Flash Card", font=("Arial", 60, "bold"))
next_card()
window.mainloop()

