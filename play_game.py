import tkinter as tk
from tkinter import ttk
from test_game import WordleApp

def play():
    game_window = tk.Toplevel()
    game_window.title("Let's Play Wordle!")
    game_window.geometry("600x800")