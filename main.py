#mywinecave version 1.0

import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyWineCave")

        label = tk.Label(self, text="Hello World!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


if __name__ == "__main__":
    window = Window()
    window.mainloop()