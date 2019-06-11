import tkinter as tk


class MathGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Math Trivia Game")
        label.pack(side="top", fill="x", pady=10)
   