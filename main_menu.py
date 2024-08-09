"""Displays the logo, creates functional buttons, displays credits."""
import tkinter as tk
from tkinter import ttk
from how_to import HowToPlay
from game import WordleApp


class WordleMainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Wordle - Main Menu")
        self.root.geometry("600x800")
        self.root.configure(bg="#F0F0F0")

        self.setup_styles()
        self.create_logo()
        self.create_buttons()
        self.create_credits()

        self.root.mainloop()

    def setup_styles(self):
        # Defines styles for labels and buttons
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.style.configure(
            "TButton", 
            font=("Helvetica", 20, "bold"), 
            padding=10
        )
        
        self.style.configure(
            "TLabel", 
            font=("Helvetica", 24, "bold"), 
            background="#F0F0F0"
        )

    def create_logo(self):
        # Programmatically creates Wordle logo, buttons, and credits
        logo_frame = ttk.Frame(self.root, style="TFrame")
        logo_frame.pack(pady=50)

        logo_word = "WORDLE"
        colors = [
            "#6AAA64", "#CEB02C", "#787C7E", 
            "#6AAA64", "#CEB02C", "#787C7E"
        ]  # Wordle colors

        for num, letter in enumerate(logo_word):
            label = tk.Label(
                logo_frame, text=letter, 
                font=("Helvetica", 48, "bold"), 
                bg=colors[num], fg="white", width=2, height=1
            )
            label.grid(row=0, column=num, padx=2)
            
            # Center the text both vertically and horizontally
            label.configure(anchor="center")
            label.grid_configure(sticky="news")

    def create_buttons(self):
        # Makes functional button widgets
        play_button = ttk.Button(
            self.root, 
            text="Play Game", 
            command=self.play_game
        )
        play_button.pack(pady=20)

        how_to_button = ttk.Button(
            self.root, 
            text="How to Play", 
            command=self.show_how_to
        )
        how_to_button.pack(pady=20)

        quit_button = ttk.Button(
            self.root, 
            text="Quit", 
            command=self.root.quit
        )
        quit_button.pack(pady=20)

    def create_credits(self):
        # Makes credits label widget
        credits = (
            "CS1410 Final Project\n"
            "Code: Kevin Pett\n"
            "Idea: Alissia Huntzinger"
        )
        credits_label = ttk.Label(
            self.root, 
            text=credits,
            font=("Helvetica", 14),
            background="#F0F0F0",
            justify="center"
        )
        credits_label.pack(side="bottom", pady=20)

    def play_game(self):
        # Deletes the main menu window and creates a game of Wordle
        self.root.destroy()
        WordleApp()

    def show_how_to(self):
        # Creates a new window with instructions on how to play
        HowToPlay()
