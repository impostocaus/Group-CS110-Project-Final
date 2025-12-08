import tkinter as tk
from tkinter import messagebox
import random

# --------
# This is where all of the questions & answers are stored
# --------

quiz = [
    {
        "question": "1. The Teacher Evaluation Model (VAM) is considered a WMD because:",
        "choices": ["A) Shows teacher quality",
                    "B) Lacks transparency (misjudged)",
                    "C) Shows teachers' opinions",
                    "D) Improves school reputation"],
        "answer": "B"
    },
    {
        "question": "2. Which is a WMD used in recruiting?",
        "choices": ["A) Asking preferences",
                    "B) Algorithm personality hiring",
                    "C) Only face-to-face interviews",
                    "D) Job performance tests"],
        "answer": "C"
    },
    {
        "question": "3. What advertising is predatory WMD?",
        "choices": ["A) Game ads",
                    "B) Personal data targeted ads",
                    "C) Free service ads",
                    "D) Random social media ads"],
        "answer": "B"
    },
    {
        "question": "4. How does social media increase political division?",
        "choices": ["A) Shows diverse perspectives",
                    "B) Reinforces user beliefs",
                    "C) Removes political ads",
                    "D) Encourages debate"],
        "answer": "D"
    },
    {
        "question": "5. WMD insurance example:",
        "choices": ["A) Credit score + age rates",
                    "B) Same rate for all",
                    "C) Preferred entry required",
                    "D) Negotiated price"],
        "answer": "A"
    }
]

# --------
# This is GUI code
# --------

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WMD Quiz Game")
        self.root.configure(bg="#1d1f21")

        self.index = 0
        self.score = 0
        self.time_limit = 30
        self.remaining = self.time_limit

        self.start_screen()

# --------
# This is the start menu
# --------

    def start_screen(self):
        self.clear()

        title = tk.Label(self.root, text="WMD Quiz Game",
                         font=("Comic Sans MS", 26, "bold"), fg="white", bg="#1d1f21")
        title.pack(pady=40)

        start_btn = tk.Button(self.root, text="Start Quiz", font=("Arial", 16),
                              width=15, bg="#3fa34d", fg="white",
                              command=self.start_quiz)
        start_btn.pack(pady=20)

# --------
# This is how the quiz shuffles the questions and resets the score
# --------

    def start_quiz(self):
        self.index = 0
        self.score = 0
        random.shuffle(quiz)
        self.show_question()

# --------
# This displays the questions and answer buttons and the timer
# --------

    def show_question(self):
        self.clear()

        q = quiz[self.index]

        self.question_label = tk.Label(self.root, text=q["question"],
                                       font=("Comic Sans MS", 16, "bold"),
                                       fg="white", bg="#1d1f21", wraplength=500)
        self.question_label.pack(pady=20)

# --------
#  This creates the buttons for each answer
# --------

        self.buttons = []
        for i, choice in enumerate(q["choices"]):
            btn = tk.Button(self.root, text=choice, width=40,
                            font=("Comic Sans MS", 12),
                            bg="#2e2e2e", fg="white", activebackground="#444",
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

# --------
# This is the timer for the questions
# --------

        self.remaining = self.time_limit
        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.remaining}s",
                                    font=("Comic Sans MS", 14), fg="orange", bg="#1d1f21")
        self.timer_label.pack(pady=10)
        self.update_timer()

# --------
# This is how the timer counts down
# --------

    def update_timer(self):
        if self.remaining > 0:
            self.timer_label.config(text=f"Time Left: {self.remaining}s")
            self.remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.disable_buttons()
            self.next_question()

# --------
# This is how the code checks if the answer is correct
# --------

    def check_answer(self, i):
        q = quiz[self.index]
        selected = q["choices"][i][0]


        if selected == q["answer"]:
            self.buttons[i].config(bg="#3fa34d")
            self.score += 1
        else:
            self.buttons[i].config(bg="#d9534f")
        self.disable_buttons()
        self.root.after(1000, self.next_question)

# --------
# This disables the quiz on the current question after the answer or if the timer runs out
# --------

    def disable_buttons(self):
        for b in self.buttons:
            b.config(state="disabled")

# --------
# This moves the quiz on to the next question
# --------

    def next_question(self):
        self.index += 1
        if self.index < len(quiz):
            self.show_question()
        else:
            self.end_screen()

# --------
# This is the score screen at the end
# --------

    def end_screen(self):
        self.clear()

        result = tk.Label(self.root, text=f"Final Score: {self.score}/{len(quiz)}",
                          font=("Arial", 22, "bold"), fg="white", bg="#1d1f21")
        result.pack(pady=40)

        restart = tk.Button(self.root, text="Play Again", font=("Arial", 16),
                            width=15, bg="#0275d8", fg="white",
                            command=self.start_quiz)
        restart.pack(pady=10)

        exit_btn = tk.Button(self.root, text="Exit", font=("Arial", 16),
                             width=15, bg="#d9534f", fg="white",
                             command=self.root.quit)
        exit_btn.pack(pady=10)

# --------
# This clears the widgets from the window
# --------

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# --------
# This allows the start of the application
# --------

root = tk.Tk()
root.geometry("600x500")
app = QuizGUI(root)
root.mainloop()
