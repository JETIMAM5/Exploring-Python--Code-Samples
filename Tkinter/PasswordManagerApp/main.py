from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("data.json", "r") as data_file:
            # Reading the old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
        with open("data.json", "w") as data_file:
            # Saving Updated data
            json.dump(data, data_file, indent=4)
            print(data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# labels
website_label = Label(window, text='Website:')
email_label = Label(window, text='Email/Username:')
password_label = Label(window, text='Password:')
website_label.grid(row=1, column=0, sticky="E")
email_label.grid(row=2, column=0, sticky="E")
password_label.grid(row=3, column=0, sticky="E")

# Entries
website_entry = Entry(window, width=35)
email_entry = Entry(window, width=35, )
password_entry = Entry(window, width=21)
email_entry.insert(0, "berat@outlook.com")
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(window, text="Generate Password", command=generate_password)
add_button = Button(window, text="Add", width=36, command=save)
generate_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


window.mainloop()
