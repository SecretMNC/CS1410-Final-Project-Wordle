"""Creates and runs the Wordle game interface."""
import tkinter as tk
from tkinter import ttk
from typing import Generator


class Game:



    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('400x800')
        self.root.resizable(False, False)
        self.root.title("Wordle")

        self.font = ()

        self.guess_container = ttk.Frame(self.root, takefocus = True)
        self.guess_container["padding"] = (62, 20, 0, 20)
        self.guess_container.columnconfigure(0, weight = 1)
        self.guess_container.columnconfigure(1, weight = 0)
        self.guess_container.columnconfigure(2, weight = 0)
        self.guess_container.columnconfigure(3, weight = 0)
        self.guess_container.columnconfigure(4, weight = 0)
        self.guess_container.columnconfigure(5, weight = 0)
        self.guess_container.columnconfigure(6, weight = 1)
        self.guess_container.grid(sticky = "we")

        self.current_guess: list[tk.StringVar] = self.build_stringvars()
        
        self._guess_num = 0
        while self._guess_num < 5:
            self.build_guess(self._guess_num)
            self._guess_num += 1
            



        self.root.mainloop()

    @staticmethod
    def build_stringvars() -> list[tk.StringVar]:
        entry_0 = tk.StringVar()
        entry_1 = tk.StringVar()
        entry_2 = tk.StringVar()
        entry_3 = tk.StringVar()
        entry_4 = tk.StringVar()

        return [entry_0, entry_1, entry_2, entry_3, entry_4]


    def build_word(self) -> Generator[tk.Entry, tk.Entry, tk.Entry]:
        for _ in range(5):
            txt_var: str = 'entry_' + str(_ + self._guess_num)
            yield ttk.Entry(self.guess_container,
                           textvariable = txt_var,
                           justify= "center",
                           font = ('calibre', 20, 'normal'),
                           width = 2)

    def build_guess(self, row_):
        """Assembles the game space with guess squares"""

        #for row_ in range(1, 7):
        char_1, char_2, char_3, char_4, char_5 = self.build_word()
        
        char_1.grid(row = row_, column = 1, padx = 10, pady = 25)
        char_2.grid(row = row_, column = 2, padx = 10, pady = 25)
        char_3.grid(row = row_, column = 3, padx = 10, pady = 25)
        char_4.grid(row = row_, column = 4, padx = 10, pady = 25)
        char_5.grid(row = row_, column = 5, padx = 10, pady = 25)

    def play_game(self):
        #while True:
        pass
            
            
        
            
    
    def check_guess(self):
        """Reads the most recent word and sends it to be checked."""
        ...



if __name__ == "__main__":
    game = Game()
