import tkinter as tk
from history.HistoryGUI import*
from history.Trivia import*
from Math.MathGUI import*

class TriviaGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        for frame in (InitPage, HistoryGUI, MathGUI):
            page_name = frame.__name__
            frame = frame(parent = container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("InitPage")
        self.title("Welcome to the Trivia Game.")


    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()

class InitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
 
        label = tk.Label(self, text="Welcome to the Trivia Game.",font = "Helvetica 16 bold italic")
        label.pack(side="top", fill="x", pady=10)

        historyButton = tk.Button(self, text="History", command=lambda: controller.show_frame("HistoryGUI"))
        historyButton.config( height = 2, width = 20 )
        historyButton.pack()        

        mathButton = tk.Button(self, text="Math Trivia", command=lambda: controller.show_frame("MathGUI"))
        mathButton.config( height = 2, width = 20 )
        mathButton.pack()

        chemButton = tk.Button(self, text="Chemistry Trivia")
        chemButton.config( height = 2, width = 20 )
        chemButton.pack()

        quitButton = tk.Button(self, text="Quit", command= self.quit_program)
        quitButton.config( height = 2, width = 20 )
        quitButton.pack()
        
    
    def quit_program(self):
        exit()         

if __name__ == "__main__":
    app = TriviaGame()
    #size of the window
    app.geometry("850x600") 
    app.mainloop()
    
