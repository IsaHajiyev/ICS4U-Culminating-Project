from tkinter import *
import tkinter as tk
from history.Trivia import*

def scroll_config(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=400)
    
class ChemGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Chemistry Trivia Game")
        label.pack(side="top", fill="x", pady=10)
        
        header = tk.Frame(self)
        header.pack(side="top", fill="both")
        
        label = tk.Label(header, text="\t\t\t\tPlease select your grade.")
        label.pack(side="left", fill="x", anchor="e", pady=10)        
        
        
        spacer = tk.Label(header, text="\t\t\t\t")
        spacer.pack(side="right", anchor="w")
        
        tk_grade_var = tk.StringVar(self)
        data = {'9','10','11','12'}
        tk_grade_var.set('10') #set the default option
          
        gradeMenu = tk.OptionMenu(header, tk_grade_var, *sorted(data), command=lambda item=tk_grade_var: gradeMenu_callback(item))
        gradeMenu.pack(side="right", anchor="w") 
        
        grade = 10
        file_name="Chemistry/chemistry_questions.txt"
        
        points = 2
        score = 0
        
        trivia = Trivia(int(grade))
        
        restart_button = tk.Button(self, text="Return to the main screen", command=self.restart)
        restart_button.config( height = 2, width = 20 )
        restart_button.pack()
        
        frame=tk.Frame(self)
        frame.pack(side="top", fill="both")
        
        canvas=Canvas(frame)
        form=Frame(canvas)
        
        scrollbar1 = Scrollbar(frame, orient="vertical",command=canvas.yview)
        scrollbar1.pack(side = "right", fill = "y")
        scrollbar2 = Scrollbar(frame, orient="horizontal",command=canvas.xview)
        scrollbar2.pack(side = BOTTOM, fill = "x")
        
        canvas.pack(side="top")
        
        canvas.create_window((0,0),window=form,anchor='nw')        
        canvas.configure(yscrollcommand=scrollbar1.set)        
        
        trivia.readFile(file_name)
        
        finalList = list(zip(trivia.questList, trivia.answList))

        for i in range(len(finalList)):
            arr = finalList[i]

            fm = tk.Frame(form)
            
            label = tk.Label(fm, text=" " + arr[0])
            label.pack(side="left", anchor="w", pady="10")  
           
            label1 = tk.Label(fm, text=" ")
            label1.pack(side="right", anchor="w") 
            

            tkvar = tk.StringVar(self)

            choices = {'A', 'B', 'C', 'D'}
            tkvar.set('---')
            
            popupMenu = tk.OptionMenu(fm, tkvar, *sorted(choices))
            popupMenu.pack(side="right", anchor="e", pady="10") 

            fm.pack(side="top", fill="both")

        form.bind("<Configure>", lambda event, canvas=canvas: scroll_config(event, canvas))  
        
    def restart(self):
        self.controller.show_frame("InitPage")
        