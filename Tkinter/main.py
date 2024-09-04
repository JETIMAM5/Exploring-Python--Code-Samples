from tkinter import *


def button_clicked():
    my_label.config(text=input0.get())


window = Tk()
window.title('GUI')
window.minsize(500, 300)
window.config(padx=20, pady=20)


# COMPONENTS
# Label

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# It's not enough to just create a label or a component ,
# also we need to specify how this component laid out on the screen
my_label["text"] = "New Text"  # we can change the kwargs like this or like the line below
my_label.config(text="New Text")
# my_label.place(x=100, y=200) # Specific coordinate of a component
# my_label.pack()  # This pack method is going to center our label
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button

button = Button(text="Click Me", command=button_clicked)
# button.pack
button.grid(column=1, row=1)
#
# # Entry
#

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

input0 = Entry(width=10)
# input0.pack()
input0.grid(column=2, row=3)


window.mainloop()
