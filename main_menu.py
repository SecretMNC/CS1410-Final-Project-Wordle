import tkinter as tk
from tkinter import ttk

class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Main Menu")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=800, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        for F in (MainMenu, HowToPlay, Game):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()
    
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wordle")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Quit Game",
            # command=lambda: controller.show_frame(MainMenu),
            command=lambda: quit()
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        switch_window_button = tk.Button(
            self,
            text="How To Play",
            command=lambda: controller.show_frame(HowToPlay),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        switch_window_button = tk.Button(
            self,
            text="Start Game",
            command=lambda: controller.show_frame(Game),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Let's Play Wordle!")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Return to Main Menu",
            command=lambda: controller.show_frame(MainMenu),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class HowToPlay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="How to play Wordle")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to main menu", command=lambda: controller.show_frame(MainMenu)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()