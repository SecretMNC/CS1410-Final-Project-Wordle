from tkinter import ttk, Tk


class Window(ttk, Tk):
    def __init__(self):
        super().__init__()

        
        self.title("Hello World")

        self.button = Button(text="My simple app.")
        self.button.bind("<MousePress>", self.on_closing)
        self.button.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()
        print("Calculator has closed.")

# Start the event loop.
window = Window()
window.mainloop()