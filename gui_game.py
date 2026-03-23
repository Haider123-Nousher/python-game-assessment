# I acknowledge the use of ChatGPT (OpenAI) to assist in creating this code.
# GUI improved version for better user experience and clarity

import random
import tkinter as tk
from tkinter import messagebox


class GuessingGameGUI:
    """GUI-based Number Guessing Game using Tkinter."""

    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game - GUI Version")

        self.max_attempts = 10
        self.reset_game()

        self.create_widgets()

    def create_widgets(self):
        """Create and layout GUI components."""

        # Title label
        tk.Label(
            self.master,
            text="Guess a number between 1 and 100",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Attempts label
        self.attempts_label = tk.Label(
            self.master,
            text=f"Attempts remaining: {self.max_attempts}",
            font=("Arial", 11)
        )
        self.attempts_label.pack()

        # Input field
        self.entry = tk.Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Guess button
        tk.Button(
            self.master,
            text="Submit Guess",
            font=("Arial", 12),
            command=self.check_guess
        ).pack(pady=5)

        # Feedback label
        self.feedback = tk.Label(
            self.master,
            text="Enter your guess to begin",
            font=("Arial", 12)
        )
        self.feedback.pack(pady=10)

        # Reset button
        tk.Button(
            self.master,
            text="Start New Game",
            font=("Arial", 12),
            command=self.reset_game_ui
        ).pack(pady=5)

    def check_guess(self):
        """Handle guess submission."""
        guess_text = self.entry.get().strip()

        # Input validation
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

        # Game logic
        if guess == self.secret_number:
            messagebox.showinfo("Correct", "You guessed the number correctly.")
            self.reset_game_ui()

        elif self.attempts >= self.max_attempts:
            messagebox.showinfo(
                "Game Over",
                f"No attempts left. The number was {self.secret_number}."
            )
            self.reset_game_ui()

        elif guess < self.secret_number:
            self.feedback.config(text="Too low. Try a higher number.")

        else:
            self.feedback.config(text="Too high. Try a lower number.")

        self.entry.delete(0, tk.END)

    def reset_game(self):
        """Reset game logic variables."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def reset_game_ui(self):
        """Reset both game logic and UI."""
        self.reset_game()
        self.feedback.config(text="Enter your guess to begin")
        self.entry.delete(0, tk.END)
        self.attempts_label.config(text=f"Attempts remaining: {self.max_attempts}")


def main():
    """Run the GUI application."""
    root = tk.Tk()
    root.geometry("360x260")
    app = GuessingGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()