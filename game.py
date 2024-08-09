"""Contains GUI and game functionality logic for a game of Wordle.
Each game produces a new, random word from a list of 580 words.
Run this module to skip the main menu and play immediately."""
import tkinter as tk
from tkinter import ttk
from random_word import WordPicker
from typing import List


class WordleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Wordle!")
        self.root.configure(bg="#F0F0F0")

        # Create a WordPicker instance and get the word and difficulty
        picker = WordPicker()
        self.word, self.diff = picker.get_word_and_difficulty()

        self.guess_num = 0
        self.current_col = 0

        self.setup_styles()
        self.create_grid()

        self.root.mainloop()

    def setup_styles(self):
        # Create styles for various states of guess boxes
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TEntry", font=("Helvetica", 96))
        self.style.configure(
            "Correct.TEntry", foreground="white", fieldbackground="#6AAA64"
        )
        self.style.configure(
            "Present.TEntry", foreground="white", fieldbackground="#C9B458"
        )
        self.style.configure(
            "Absent.TEntry", foreground="white", fieldbackground="#787C7E"
        )
        self.style.map(
            "Correct.TEntry", fieldbackground=[("readonly", "#6AAA64")]
        )
        self.style.map(
            "Present.TEntry", fieldbackground=[("readonly", "#C9B458")]
        )
        self.style.map(
            "Absent.TEntry", fieldbackground=[("readonly", "#787C7E")]
        )

    def create_grid(self) -> None:
        # Sets up 5 by 6 grid of Entry boxes, ready to handle inputs
        self.entries = []
        for row in range(6):
            row_entries = []
            for col in range(5):
                entry = ttk.Entry(
                    self.root, width=2, justify="center", style="TEntry"
                )
                entry.grid(row=row, column=col, padx=4, pady=10)
                entry.bind(
                    "<KeyRelease>",
                    lambda event, row_=row, col_=col: self.handle_input(
                        event, row_, col_
                    ),
                )
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Set focus on the first entry of the first row
        self.entries[0][0].focus_set()

    def handle_input(self, event, row, col) -> None:
        entry = self.entries[row][col]
        value = entry.get().upper()

        if event.keysym == "BackSpace":
            if col > 0 and not value:
                self.entries[row][col - 1].focus_set()
                self.entries[row][col - 1].delete(0, tk.END)
            return

        if not value:
            return

        # Ensure only the first character is kept
        value = value[0]

        if not value.isalpha():
            entry.delete(0, tk.END)
            return

        entry.delete(0, tk.END)
        entry.insert(0, value)

        if col < 4:
            self.entries[row][col + 1].focus_set()
        else:
            self.check_guess(row)

    def check_guess(self, row) -> None:
        guess = "".join(entry.get().upper() for entry in self.entries[row])

        if len(guess) != 5:
            return

        check = [0] * 5
        letter_used = [False] * 5

        # First pass: check for correct letters in correct positions
        for index, char in enumerate(guess):
            if self.word[index] == char:
                check[index] = 2
                letter_used[index] = True

        # Second pass: check for correct letters in wrong positions
        for index, char in enumerate(guess):
            if check[index] == 0:  # Only check if not already marked correct
                for j, w_char in enumerate(self.word):
                    if not letter_used[j] and char == w_char:
                        check[index] = 1
                        letter_used[j] = True
                        break

        self.update_colors(row, check)
        self.guess_num += 1
        result = self.check_win(check)

        if self.guess_num < 6 and not result:
            for entry in self.entries[self.guess_num]:
                entry.config(state="normal")
            self.entries[self.guess_num][0].focus_set()

    def update_colors(self, row, checker: List[int]) -> None:
        styles = {0: "Absent.TEntry", 1: "Present.TEntry", 2: "Correct.TEntry"}
        for index, entry in enumerate(self.entries[row]):
            entry.config(style=styles[checker[index]], state="readonly")

    def check_win(self, checker: List[int]) -> bool:
        if all(c == 2 for c in checker):
            self.show_result("You win!")
            return True
        elif self.guess_num >= 6:
            self.show_result(f"The word was \n{self.word}.")
            return False
        return False

    def show_result(self, message: str) -> None:
        result_label = tk.Label(
            self.root, text=message, font=("Helvetica", 12, "bold"), bg="#F0F0F0"
        )
        result_label.grid(row=7, column=0, columnspan=5, pady=20)
        retry_button = ttk.Button(
            self.root, text="Play again", command=self.reset
        )
        retry_button.grid(row=8, column=0, columnspan=5, pady=20)

    def reset(self) -> None:
        self.root.destroy()
        WordleApp()


if __name__ == "__main__":
    app = WordleApp()
