import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk
from tkinter import PhotoImage
from how_to import HowToPlay
from play_game import play

class Windows(tk.Tk):
    def __init__(self):
         # Inheriting from tk.Tk, adding a title, and setting sizes of the window
        super().__init__()
        self.wm_title("Main Menu")
        self.geometry("600x800")
        self.resizable(False, False)

        #  Image 
        self.logo = PhotoImage(file="assets/wordle_logo_resized.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack()

        # Place byline and button widgets
        self.menu = Menu(self)

        #run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.make_widgets()
    
    def make_widgets(self):
        #define widget container on frame
        self.pack()

        #create byline widgets
        makers_1 = ttk.Label(self, text="\n\n\nCS1410 Final Project\n", justify="center", font=('Helvetica', 28))
        makers_2 = ttk.Label(self, text="by\n\nKevin Pett & Alissia Austell Huntzinger\n\n", justify="center")
        
        #place byline widgets in container
        makers_1.pack()
        makers_2.pack()

        #create button widgets
        how_btn = ttk.Button(self, text="How to Play", command=HowToPlay)
        play_btn = ttk.Button(self, text="Play Game", command=play)
        close_btn = ttk.Button(self, text="Close", command=self.quit)

        #place widgets in container
        how_btn.pack(side='left')
        play_btn.pack(side='left')
        close_btn.pack(side='left')

if __name__ == "__main__":
    w = Windows()
