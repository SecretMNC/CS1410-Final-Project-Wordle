import tkinter as tk
from tkinter import messagebox
from random_word import WordPicker

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle!")

        # Create a WordPicker instance and get the word and difficulty
        picker = WordPicker()
        self.word, self.diff = picker.get_word_and_difficulty()

        self.guess: str
        self.guess_num = 0

        self.create_grid()

        self.entry = tk.Entry(self.root)
        self.entry.bind("<KeyPress>", self.keyboard)
        self.entry.grid(row=6, column=0, columnspan=5)

        self.submit_button = tk.Button(self.root, 
                                       text="Submit", 
                                       command=self.check_guess)
        self.submit_button.grid(row=7, column=0, columnspan=5)

    def create_grid(self) -> None:
        # Creates the empty guess boxes at the start of a game
        self.labels: list[list[tk.Label]] = []
        for row in range(6):
            row_labels: list[tk.Label] = []
            for col in range(5):
                label = tk.Label(self.root, 
                                 text="", 
                                 width=2, 
                                 height=1, 
                                 font=("Helvetica", 24), 
                                 borderwidth=2, 
                                 relief="solid")
                label.grid(row=row, column=col)
                row_labels.append(label)
            self.labels.append(row_labels)

    def check_guess(self) -> None:
        """Checks each character of the guess against each char of the word."""
        self.guess = self.entry.get().upper()
        if not self.invalid_guess():
            return None

        check: list[int] = [0] * 5
        letter_used = [False] * 5  # Track which letters in the word have been used

        # First pass: check for exact matches (green)
        for index, char in enumerate(self.guess):
            if self.word[index] == char:
                check[index] = 2
                letter_used[index] = True

        # Second pass: check for correct letters in wrong position (yellow)
        for index, char in enumerate(self.guess):
            if check[index] == 0:  # Only process if not green
                for j, w_char in enumerate(self.word):
                    if not letter_used[j] and char == w_char:
                        check[index] = 1
                        letter_used[j] = True
                        break

        self.update_labels(check)
        self.guess_num += 1
        self.check_win(check)
        if self.guess_num < 6:
            self.guess = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.guess)


    def invalid_guess(self) -> bool:
        if list(filter(lambda x: not x.isalpha(), self.guess)):
            messagebox.showinfo(title="Character warning",
                                message="Guesses may only contain letters.")
            self.guess = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.guess)
            return False
        elif len(self.guess) <= 0:
            return False
        elif len(self.guess) != 5:
            messagebox.showinfo(title="Length warning",
                                message="Guesses may only be 5 letters long.")
            self.guess = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.guess)
            return False
        else:
            return True

    def update_labels(self, checker: list[int]) -> None:
        # Takes the guess checker list and updates the letter grid
        for index, _ in enumerate(self.labels[self.guess_num]):
            #print(f"Index {index}, letter {self.guess[index]}")
            if checker[index] == 2:
                color = "green"
            elif checker[index] == 1:
                color = "yellow"
            elif checker[index] == 0:
                color = "white"
            new_label = tk.Label(self.root, 
                                 text=self.guess[index], 
                                 width=2, 
                                 height=1, 
                                 font=("Helvetica", 24), 
                                 borderwidth=2, 
                                 relief="solid", 
                                 bg=color)
            new_label.grid(row=self.guess_num, column=index)
            
    def check_win(self, checker: list[int]) -> None:
        # Checks if a win or loss condition has been met
        if not list(filter(lambda x: x != 2, checker)):
            self.result_label = tk.Label(self.root, 
                                 text="You win!", 
                                 height=1, 
                                 font=("Helvetica", 24), 
                                 borderwidth=2)
            self.entry.destroy()
            self.submit_button.destroy()
            self.retry_button = tk.Button(self.root,
                                    text="Play again?", 
                                    command=self.reset)
            self.retry_button.grid(row=7, column=0, columnspan=5)
            self.result_label.grid(row=8, column=0, columnspan=5)
        elif self.guess_num >= 6:
            self.result_label = tk.Label(self.root, 
                                 text=f"The word was {self.word}.", 
                                 height=1, 
                                 font=("Helvetica", 12), 
                                 borderwidth=2)
            self.entry.destroy()
            self.submit_button.destroy()
            self.retry_button = tk.Button(self.root,
                                    text="Try another?", 
                                    command=self.reset)
            self.retry_button.grid(row=7, column=0, columnspan=5)
            self.result_label.grid(row=8, column=0, columnspan=5)

    def keyboard(self, event) -> None:
        # Accepts the enter/return key in place of pressing the submit button
        if event.keysym == "Return" or event.keysym == "KP_Enter":
            self.check_guess()

    def reset(self):
        # Wipes the old game and creates a new one with a new word
        self.retry_button.destroy()
        self.result_label.destroy()

        picker = WordPicker()
        self.word, self.diff = picker.get_word_and_difficulty()

        self.guess = ""
        self.guess_num = 0

        self.create_grid()

        self.entry = tk.Entry(self.root)
        self.entry.bind("<KeyPress>", self.keyboard)
        self.entry.grid(row=6, column=0, columnspan=5)

        self.submit_button = tk.Button(self.root, 
                                    text="Submit", 
                                    command=self.check_guess)
        self.submit_button.grid(row=7, column=0, columnspan=5)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
