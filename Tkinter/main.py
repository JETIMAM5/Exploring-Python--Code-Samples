from tkinter import *

window = Tk()
window.title('GUI')
window.minsize(500, 300)


# COMPONENTS
# Label

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# It's not enough to just create a label or a component ,
# also we need to specify how this component laid out on the screen
my_label["text"] = "New Text"  # we can change the kwargs like this or like the line below
my_label.config(text="New Text")
my_label.pack()  # This pack method is going to center our label


# Button


def button_clicked():
    my_label.config(text=input0.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input0 = Entry(width=10)
input0.pack()


window.mainloop()
