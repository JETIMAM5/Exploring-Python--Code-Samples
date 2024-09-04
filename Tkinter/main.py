import tkinter

window = tkinter.Tk()
window.title('GUI')
window.minsize(500, 300)


# COMPONENTS
# Label

my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
# It's not enough to just create a label or a component ,
# also we need to specify how this component laid out on the screen
my_label.pack()  # This pack method is going to center our label

window.mainloop()
