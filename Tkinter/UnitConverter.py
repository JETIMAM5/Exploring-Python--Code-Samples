from tkinter import *

MILES_TO_KM_FACTOR = 1.609
KM_TO_MILES_FACTOR = 0.621
FONT = ('San Francisco', 20, 'normal')

window = Tk()
window.title('Unit Converter')
window.geometry('500x200')
window.config(padx=20, pady=20)


# Functions
def miles_to_kilometers():
    result = round(float(mile_input.get()) * MILES_TO_KM_FACTOR, 3)
    calculated_label.config(text=f"{result}")
    mile_label.config(text="Miles")
    km_label.config(text="Km")


def kilometers_to_miles():
    result = round(float(mile_input.get()) * KM_TO_MILES_FACTOR, 3)
    calculated_label.config(text=f"{result}")
    mile_label.config(text="Km")
    km_label.config(text="Miles")


def option_selected():
    choice = selected_option.get()
    if choice == "Miles To Kilometers":
        if mile_input.get():
            miles_to_kilometers()
    elif choice == "Kilometers To Miles":
        if mile_input.get():
            kilometers_to_miles()


# Labels
mile_label = Label(window, text='Miles', font=FONT)
mile_label.grid(row=0, column=2)

equal_label = Label(window, text='is equal to', font=FONT)
equal_label.grid(row=1, column=0)

km_label = Label(window, text='Km', font=FONT)
km_label.grid(row=1, column=2)

calculated_label = Label(window, text=0, font=FONT)
calculated_label.grid(row=1, column=1)

# Entry
mile_input = Entry(width=10, font=FONT)
mile_input.focus()
mile_input.grid(row=0, column=1)

# Button
button = Button(window, text='Calculate', font=FONT, command=option_selected)
button.grid(row=2, column=1)

# Dropdown list
selected_option = StringVar(window)
selected_option.set("Select Conversion")

conversion_types = ["Miles To Kilometers", "Kilometers To Miles"]
dropdown = OptionMenu(window, selected_option, *conversion_types)
dropdown.config(font=('San Francisco', 14, 'normal'))
dropdown.grid(row=2, column=0)

window.mainloop()
