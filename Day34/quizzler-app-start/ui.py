from tkinter import *
from tkmacosx import Button
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WHITE = "#ffffff"
FONT = ("Arial", 15)

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=FONT, fg=WHITE, bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        # Buttons

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, borderless=1, bg=THEME_COLOR, width=130, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, borderless=1, bg=THEME_COLOR, width=130, command=self.check_false)
        self.false_button.grid(row=2, column=1)
        #
        # right_img = PhotoImage(file="images/right.png")
        # right_button = Button(image=right_img, borderless=1, bg=BACKGROUND_COLOR, width=130, command=gen_wordpair_right)
        # right_button.grid(row=1, column=1)
        #
        # genpass_button = Button(text="Generate Password", borderless=1, width=130, command=generate_password)
        # genpass_button.grid(row=3, column=2, sticky='w')

        self.get_next_questions()

        self.window.mainloop()

    def get_next_questions(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_questions)


        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_questions)


