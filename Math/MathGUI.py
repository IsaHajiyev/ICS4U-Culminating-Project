import tkinter as tk


class MathGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Math Trivia Game")
        label.pack(side="top", fill="x", pady=10)
        
        restart_button = tk.Button(self, text="Return to the main screen", command=self.restart)
        restart_button.config( height = 2, width = 20 )
        restart_button.pack()
        
    def restart(self):
        #self.refresh()
        self.controller.show_frame("InitPage")                
   