"""Creates and runs the Wordle game interface."""
import tkinter as tk
from tkinter import ttk


class Game:
    def __init__(self):
        
        self.root = tk.Tk() 
        self.root.geometry('800x1000')

        self.game_frame = tk.Frame(self.root)
        self.game_frame.columnconfigure(0, weight=0)
        self.game_frame.columnconfigure(1, weight=1)
        self.game_frame.columnconfigure(2, weight=2)
        self.game_frame.columnconfigure(3, weight=1)
        self.game_frame.columnconfigure(4, weight=2)
        self.game_frame.columnconfigure(5, weight=1)
        self.game_frame.columnconfigure(6, weight=2)
        self.game_frame.columnconfigure(7, weight=1)
        self.game_frame.columnconfigure(8, weight=2)
        self.game_frame.columnconfigure(9, weight=1)
        self.game_frame.columnconfigure(10, weight=0)
        self.game_frame.pack(fill="both")

        self.c_1 = tk.StringVar()
        self.c_2 = tk.StringVar()
        self.c_3 = tk.StringVar()
        self.c_4 = tk.StringVar()
        self.c_5 = tk.StringVar()


        self.build_game()
        self.root.mainloop()

    def check_guess(self):
        
        char_1 = self.c_1.get()
        char_2 = self.c_1.get()
        char_3 = self.c_1.get()
        char_4 = self.c_1.get()
        char_5 = self.c_1.get()

        self.c_1.set("")
        self.c_2.set("")
        self.c_3.set("")
        self.c_4.set("")
        self.c_5.set("")

    def build_game(self):
        """Assembles the game space with guess squares"""
        self.horz_spacer1 = tk.Label(self.game_frame, text="")
        self.horz_spacer1.grid(row=0, column=1)
        self.horz_spacer2 = tk.Label(self.game_frame, text="")
        self.horz_spacer2.grid(row=6, column=1)

        self.vert_spacer1 = tk.Label(self.game_frame, text="")
        self.vert_spacer1.grid(column=0, row=1, rowspan=6)
        self.vert_spacer2 = tk.Label(self.game_frame, text="")
        self.vert_spacer2.grid(column=6, row=1, rowspan=6)

        self.spacer = tk.Label(self.game_frame, text="")
        self.spacer.grid(row=1, column=2)
        self.spacer2 = tk.Label(self.game_frame, text="")
        self.spacer2.grid(row=1, column=4)

        self.c1r0 = tk.Entry(self.game_frame, textvariable=self.c_1, bg="white", justify="center", relief="flat")
        self.c1r0.grid(row=1, column=1)
        self.c2r0 = tk.Entry(self.game_frame, textvariable=self.c_2, bg="white", justify="center", relief="flat")
        self.c2r0.grid(row=1, column=3)
        self.c3r0 = tk.Entry(self.game_frame, textvariable=self.c_3, bg="white", justify="center", relief="flat")
        self.c3r0.grid(row=1, column=5)
        self.c4r0 = tk.Entry(self.game_frame, textvariable=self.c_4, bg="white", justify="center", relief="flat")
        self.c4r0.grid(row=1, column=7)
        self.c5r0 = tk.Entry(self.game_frame, textvariable=self.c_5, bg="white", justify="center", relief="flat")
        self.c5r0.grid(row=1, column=9)


if __name__ == "__main__":
    game = Game()
