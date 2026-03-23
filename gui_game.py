# I acknowledge the use of ChatGPT (OpenAI) to assist in creating this code.
# Final merge fix change and GUI refinement

import random
import tkinter as tk
from tkinter import messagebox


class GuessingGameGUI:
    """GUI-based Number Guessing Game using Tkinter."""

    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game - Final Version")

        self.max_attempts = 10
        self.reset_game()

        self.create_widgets()

    def create_widgets(self):
        """Create GUI components."""

        tk.Label(
            self.master,
            text="Guess a number between 1 and 100",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.attempts_label = tk.Label(
            self.master,
            text=f"Attempts remaining: {self.max_attempts}",
            font=("Arial", 11)
        )
        self.attempts_label.pack()

        self.entry = tk.Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=10)

        tk.Button(
            self.master,
            text="Submit Guess",
            command=self.check_guess
        ).pack(pady=5)

        self.feedback = tk.Label(
            self.master,
            text="Enter your guess to start",
            font=("Arial", 12)
        )
        self.feedback.pack(pady=10)

        tk.Button(
            self.master,
            text="New Game",
            command=self.reset_game_ui
        ).pack(pady=5)

    def check_guess(self):
        """Process the user's guess."""
        guess_text = self.entry.get().strip()

        if not guess_text:
            self.feedback.config(text="Please enter a number.")
            return

        if not guess_text.isdigit():
            self.feedback.config(text="Invalid input. Enter a whole number.")
            return

        guess = int(guess_text)

        if not (1 <= guess <= 100):
            self.feedback.config(text="Number must be between 1 and 100.")
            return

        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts remaining: {remaining}")

        if guess == self.secret_number:
            messagebox.showinfo("Correct", "You guessed correctly.")
            self.reset_game_ui()

        elif self.attempts >= self.max_attempts:
            messagebox.showinfo(
                "Game Over",
                f"No attempts left. Number was {self.secret_number}."
            )
            self.reset_game_ui()

        elif guess < self.secret_number:
            self.feedback.config(text="Too low.")
        else:
            self.feedback.config(text="Too high.")

        self.entry.delete(0, tk.END)

    def reset_game(self):
        """Reset game variables."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def reset_game_ui(self):
        """Reset game and UI."""
        self.reset_game()
        self.feedback.config(text="Enter your guess to start")
        self.entry.delete(0, tk.END)
        self.attempts_label.config(text=f"Attempts remaining: {self.max_attempts}")


def main():
    """Run the GUI game."""
    root = tk.Tk()
    root.geometry("360x250")
    GuessingGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()