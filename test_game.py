import tkinter as tk
from tkinter import messagebox
from parse_words import WordPicker

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle!")
        self.word = "POKER"
        #self.word, self.diff = WordPicker()
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
        """Checks each character of the guess against each char of the word.
        1: If the character matches in the exact index, append a '2' to a list
        2: If the character exists but it's already been guessed right AND 
        the char isn't in the remaining indexes, append a '0'
        3: If the character exists but it's in the wrong index, append a '1'
        4: Else append a '0' """
        self.guess: str = self.entry.get().upper()
        if not self.invalid_guess():
            return None

        def check_if_already_right(index, char) -> bool:
            # Checks if the given character was already guessed correctly
            if check[index] == 2 and self.word[index] == char:
                return True

        check: list[int] = []
        for index, char in enumerate(self.guess):
            if self.word[index] == char:
                check.append(2)
            elif [x for x in range(index) if check_if_already_right(x, char)] \
                and char not in self.word[index:]:
                check.append(0)
            elif char in self.word:
                check.append(1)
            else:
                check.append(0)

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
                                    text="Try again?", 
                                    command=self.reset)
            self.retry_button.grid(row=7, column=0, columnspan=5)
            self.result_label.grid(row=8, column=0, columnspan=5)

    def keyboard(self, event) -> None:
        # Accepts the enter/return key in place of pressing the submit button
        guess_len: int = len(self.entry.get())
        if event.keysym == "Return" or event.keysym == "KP_Enter" \
        and guess_len == 5 and self.guess_num < 6:
            self.check_guess()

    def reset(self):
        self.retry_button.destroy()
        self.result_label.destroy()
        self.word = "RANDO"
        self.guess: str = ""
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
