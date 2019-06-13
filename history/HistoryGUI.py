from tkinter import *
import tkinter as tk
from history.Trivia import*
import random


grade_idx = list()

def scroll_config(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=400) 

def gradeMenu_callback(item):
    print("value is:" + str(item))
    grade = item
    pass

class HistoryGUI(tk.Frame):
       
    def data(self, frame):
        for i in range(150):
            tk.Label(frame,text=i).grid(row=i,column=0)
            tk.Label(frame,text="my text"+str(i)).grid(row=i,column=1)
            tk.Label(frame,text="..........").grid(row=i,column=2)
        

        
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
          
        gradeMenu = tk.OptionMenu(header, tk_grade_var, *sorted(data), command=lambda item=tk_grade_var: gradeMenu_callback(item))
        gradeMenu.pack(side="right", anchor="w") 

        
        #Questions
        
        print('Starting the trivia program.')
        #grade = input('Please enter your grade:')
        grade = 10
        file_name="history/history_questions.txt"
        
        points = 2
        score = 0 
        
        #Call the class constructor.
        trivia = Trivia(int(grade))
        
        #Read the file and load the corresponding
        #array
        trivia.readFile(file_name)
        
        if not int(grade) in trivia.gradeList:
            print('Grade is not supported, please select a different grade.')
            exit()
            
        print('Please provide your answers in A, B or C format.')    
        
        finalList = list(zip(trivia.questList, trivia.answList))
        
        #use random to shuffle the zipped list
        random.shuffle(finalList)
       
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
            tkvar = tk.StringVar(self)

            choices = { 'True','False'}
            tkvar.set('---') # set the default option
            
            popupMenu = tk.OptionMenu(fm, tkvar, *choices)
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
        
        