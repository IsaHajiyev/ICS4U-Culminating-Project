from tkinter import *
import tkinter as tk
from history.Trivia import*
import random

grade = 10
trivia = Trivia(int(grade))
#grade_idx = list()

file_name="history/history_questions.txt"

def show_frame(self, page_name):
    for frame in self.frames.values():
        frame.grid_remove()
    frame = self.frames[page_name]
    frame.grid()
    return frame


def scroll_config(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"),width=800,height=400) 

def get_grade():
    return grade


def scoreMenu_callback(guess, answer, idx):
    print ("------------score menu-------guess:" + guess + " --answer:" + answer + " --index:" + str(idx))
    
def gradeMenu_callback(self, item, frame, controller):
    print("value is:" + str(item))
    grade = item
    trivia = Trivia(int(grade))
    trivia.readFile(file_name)
    finalList = list(zip(trivia.questList, trivia.answList))
    print(finalList)
    #clear the grid
    #frame.pack_forget()
    #frame.grid_forget()
    #frame.destroy()
 
    for widget in frame.winfo_children():
        widget.destroy()

    canvas=Canvas(frame)

    form=Frame(canvas)
    
    for widget in form.winfo_children():
        widget.destroy() 
    
    '''   
    for widget in canvas.winfo_children():
            widget.destroy()           

    for widget in frame.winfo_children():
        widget.destroy()    
    '''
    scrollbar = Scrollbar(frame, orient="vertical",command=canvas.yview)

    scrollbar.pack(side = "right", fill = "y" )        

    canvas.pack(side="top")

    canvas.create_window((0,0),window=form,anchor='nw')        
    canvas.configure(yscrollcommand=scrollbar.set)        


    for i in range(len(finalList)):
        arr= finalList[i]
        #print(arr[0])

        fm = tk.Frame(form)

        label = tk.Label(fm, text=" " + arr[0])
        label.pack(side="left", anchor="w", pady="10")  

        label1 = tk.Label(fm, text=" ")
        label1.pack(side="right", anchor="w") 

        # Create a Tkinter variable
        tkvar = tk.StringVar(self)

        choices = {'True','False'}
        tkvar.set('Select') # set the default option
        
        print(tkvar.get())
        
        popupMenu = tk.OptionMenu(fm, tkvar, *choices)
        popupMenu.pack(side="right", anchor="e", pady="10") 

        #fm.pack(side="top", anchor="w")
        fm.pack(side="top", fill="both")

        frame.pack(side="top", fill="both")

    form.bind("<Configure>", lambda event, canvas=canvas: scroll_config(event, canvas))
    pass       


def get_trivia(grade):
    trivia = Trivia(int(grade))
    
    return trivia


class HistoryGUI(tk.Frame):
    print("----------------init--------------")  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="History Trivia Game",font = "Helvetica 12 bold italic")
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
          
        gradeMenu = tk.OptionMenu(header, tk_grade_var, *sorted(data), command=lambda item=tk_grade_var: gradeMenu_callback(self, item, frame, controller))
        gradeMenu.pack(side="right", anchor="w") 

        
        #Questions
        
        print('Starting the trivia program.')
        #grade = input('Please enter your grade:')
        grade = get_grade()

        
        points = 2
        score = 0 
        
        #get the Trivia class.
        trivia = get_trivia(grade)
        
        #Read the file and load the corresponding
        #array
        trivia.readFile(file_name)
      
        finalList = list(zip(trivia.questList, trivia.answList))
        
        #use random to shuffle the zipped list
        #random.shuffle(finalList)
       
        frame=tk.Frame(self)
        
        frame.pack(side="top", fill="both")
        
        canvas=Canvas(frame)
        form=Frame(canvas)
        
        scrollbar = Scrollbar(frame, orient="vertical",command=canvas.yview)
        
        scrollbar.pack(side = "right", fill = "y" )        
        
        canvas.pack(side="top")
        
        canvas.create_window((0,0),window=form,anchor='nw')        
        canvas.configure(yscrollcommand=scrollbar.set)        


        for i in range(len(finalList)):
            arr= finalList[i]
            #print(arr[0])
            
            fm = tk.Frame(form)
            
            label = tk.Label(fm, text=" " + arr[0])
            label.pack(side="left", anchor="w", pady="10")  
           
            label1 = tk.Label(fm, text=" ")
            label1.pack(side="right", anchor="w") 
            
            # Create a Tkinter variable
            tk_score_var = tk.StringVar(self)

            choices = { 'True','False'}
            tk_score_var.set('Select') # set the default option
            answer = arr[1]
            popupMenu = tk.OptionMenu(fm, tk_score_var, *choices,  command=lambda item=tk_score_var: scoreMenu_callback(item, answer, i))
            popupMenu.pack(side="right", anchor="e", pady="10") 
            
             
            
            #fm.pack(side="top", anchor="w")
            fm.pack(side="top", fill="both")
                
        # frame.pack(side="top", fill="both")
        form.bind("<Configure>", lambda event, canvas=canvas: scroll_config(event, canvas))
        
        #eof Questions

        refresh_button = tk.Button(self, text="Check Score", command=self.score) 
        refresh_button.config( height = 2, width = 20 )
        refresh_button.pack()  
        
        restart_button = tk.Button(self, text="Return to the main screen", command=self.restart)
        restart_button.config( height = 2, width = 20 )
        restart_button.pack()
     
    def restart(self):
        #self.refresh()
        self.controller.show_frame("InitPage")

    def score(self):
        self.wentry.focus_set()
        
        