import tkinter as tk
from business.BusinessGUI import*
from history.HistoryGUI import*
from Math.MathGUI import*
from chem.ChemGUI import*
from english.EnglishGUI import*
from core.Trivia import*

class TriviaGame(tk.Tk): #Class displays and creates the needed space for the GUI

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        for frame in (InitPage, BusinessGUI, HistoryGUI, MathGUI, ChemGUI, EnglishGUI):
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

class InitPage(tk.Frame): #Class contains the majority of the buttons used to access the questions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
 
        label = tk.Label(self, text="Welcome to the Trivia Game.",font = "Helvetica 16 bold italic")
        label.pack(side="top", fill="x", pady=10)
        
        businessButton = tk.Button(self, text="Business Trivia", command=lambda: controller.show_frame("BusinessGUI"))
        businessButton.config(height = 2, width = 20)
        businessButton.pack()

        historyButton = tk.Button(self, text="History Trivia", command=lambda: controller.show_frame("HistoryGUI"))
        historyButton.config(height = 2, width = 20)
        historyButton.pack()        

        mathButton = tk.Button(self, text="Math Trivia", command=lambda: controller.show_frame("MathGUI"))
        mathButton.config(height = 2, width = 20)
        mathButton.pack()

        chemButton = tk.Button(self, text="Chemistry Trivia", command=lambda: controller.show_frame("ChemGUI"))
        chemButton.config(height = 2, width = 20)
        chemButton.pack()
        
        engButton = tk.Button(self, text="English Trivia", command=lambda: controller.show_frame("EnglishGUI"))
        engButton.config(height = 2, width = 20)
        engButton.pack()        

        quitButton = tk.Button(self, text="Quit", command= self.quit_program)
        quitButton.config(height = 2, width = 20)
        quitButton.pack()
        
    
    def quit_program(self): #Function exits the program
        exit()         

if __name__ == "__main__": #Determines the size of the window
    app = TriviaGame()
    #Size of the window
    app.geometry("700x600") 
    app.mainloop()