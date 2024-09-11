from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlerr")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(self.window, highlightthickness=0, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="EW", pady=50)

        # Buttons
        correct_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.correct_button = Button(self.window, image=correct_image, highlightthickness=0, bg=THEME_COLOR,
                                     command=self.correct_button_click)
        self.wrong_button = Button(self.window, image=false_image, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.wrong_button_click)
        self.correct_button.grid(row=2, column=0, sticky="EW")
        self.wrong_button.grid(row=2, column=1, sticky="EW")

        # Score Label
        self.label = Label(self.window, text=f"Score: 0", padx=10, pady=10, bg=THEME_COLOR, fg="white",
                           font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_button_click(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.quiz.next_question()

    def wrong_button_click(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.quiz.next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
