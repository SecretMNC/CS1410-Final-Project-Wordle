"""Opens a new window and displays instructions on how to play the game."""
import tkinter as tk
from tkinter import ttk


class HowToPlay:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("How to Play Wordle")
        self.root.geometry("500x800")
        self.root.configure(bg="#F0F0F0")
        self.root.resizable(False, False)

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        # Defining styles for three types of widgets
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "TLabel",
            font=("Helvetica", 14),
            background="#F0F0F0",
            justify="center",
            padding=5
        )

        self.style.configure(
            "Title.TLabel",
            font=("Helvetica", 24, "bold"),
            background="#F0F0F0",
            padding=10
        )

        self.style.configure(
            "TButton",
            font=("Helvetica", 14),
            padding=5
        )

    def create_widgets(self):
        # Creating widgets and the content of the instructions
        main_frame = ttk.Frame(
            self.root, padding="20 20 20 20", style="TFrame"
        )
        main_frame.grid(column=0, row=0, sticky="news")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(
            main_frame, text="How to Play Wordle", justify="center",
            style="Title.TLabel"
        ).grid(column=0, row=0, pady=10)

        instructions = [
            "1. Guess the Wordle in 6 tries.",
            "2. Each guess must be a valid 5-letter word.",
            "3. The color of the tiles will change to show",
            "   how close your guess was to the word.\n",
            "Color Meanings:",
            "• Green: The letter is correct and in the right spot.",
            "• Yellow: The letter is in the word but in the wrong spot.",
            "• Gray: The letter is not in the word."
        ]

        for i, instruction in enumerate(instructions):
            ttk.Label(main_frame, text=instruction, style="TLabel").grid(
                column=0, row=i + 1, sticky=tk.W
            )

        self.create_example(main_frame)

        ttk.Button(
            main_frame, text="Close", command=self.root.destroy
        ).grid(column=0, row=len(instructions) + 7, pady=20)

    def create_example(self, parent):
        # Creates an example
        example_frame = ttk.Frame(parent)
        example_frame.grid(column=0, row=11, pady=20)

        example_word = [
            ("W", "green"),
            ("E", "gray"),
            ("A", "yellow"),
            ("R", "gray"),
            ("Y", "gray")
        ]

        for i, (letter, color) in enumerate(example_word):
            bg_color = {
                "green": "#6AAA64",
                "yellow": "#C9B458",
                "gray": "#787C7E"
            }[color]
            label = tk.Label(
                example_frame,
                text=letter,
                font=("Helvetica", 20, "bold"),
                bg=bg_color,
                fg="white",
                width=2,
                height=1
            )
            label.grid(row=0, column=i, padx=2)

        ttk.Label(
            parent, text="W is in the word and in the correct spot.",
            style="TLabel"
        ).grid(column=0, row=12, sticky=tk.W)
        ttk.Label(
            parent, text="A is in the word but in the wrong spot.",
            style="TLabel"
        ).grid(column=0, row=13, sticky=tk.W)
        ttk.Label(
            parent, text="E, R, Y are not in the word in any spot.",
            style="TLabel"
        ).grid(column=0, row=14, sticky=tk.W)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    HowToPlay()
    root.mainloop()
