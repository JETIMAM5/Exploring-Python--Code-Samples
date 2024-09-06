from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    with open('data.txt', 'a') as file:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# labels
website_label = Label(window, text='Website:')
email_label = Label(window, text='Email/Username:')
password_label = Label(window, text='Password:')
website_label.grid(row=1, column=0, sticky="E")
email_label.grid(row=2, column=0, sticky="E")
password_label.grid(row=3, column=0, sticky="E")  # This grid method collaborates with sticky argument
# to align components

# Entries
website_entry = Entry(window, width=35)
website_entry.focus()  # Focuses on the website entry at the beginning
email_entry = Entry(window, width=35)
email_entry.insert(0, 'berat_yetis5859@outlook.com')  # pre populated e mail
password_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(window, text="Generate Password")
add_button = Button(window, text="Add", width=36, command=save)
generate_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


window.mainloop()
