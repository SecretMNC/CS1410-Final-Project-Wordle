import tkinter as tk
    
class HowToPlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("How to Play")

        self.instructions = (
            "Welcome to Wordle!\n\n"
            "1. Guess the 5-letter word within 6 tries.\n"
            "2. Each guess must be a valid 5-letter word.\n"
            "3. After each guess, the color of the tiles will change:\n"
            "\n   - Green: Correct letter in the correct position.\n"
            "   - Yellow: Correct letter in the wrong position.\n"
            "   - White: Incorrect letter.\n\n"
            "Good luck!"
        )

        self.show_instructions()

        self.root.mainloop()

    def show_instructions(self):
        color = "#6AAA64"
        background = tk.Frame(self.root, bg=color)
        explanation = tk.Label(background, 
                                text=self.instructions, 
                                font=("Helvetica", 20),
                                justify="left",
                                bg=color)
        background.pack()
        explanation.pack(padx=50, pady=50)
        
if __name__ == "__main__":
    how = HowToPlay()
