from tkinter import *
import tkinter as tk
from core.Trivia import*
import random

#default grade to load
grade = 10
score_index = 2
trivia = Trivia()
#grade_idx = list()

file_name="chem/chem_questions.txt"

#Show frame selected
def show_frame(self, page_name):
    for frame in self.frames.values():
        frame.grid_remove()
    frame = self.frames[page_name]
    frame.grid()
    return frame

#Show score
def check_score(labelScore):
    if(int(trivia.score) == int(trivia.max_score)):
        labelScore.config(text="Congratulations! Your score is max: " + str(trivia.score), fg = "red")
    elif(int(trivia.score) < int(trivia.max_score)/2):
        labelScore.config(text="The score is: " + str(trivia.score) + " out of " + str(trivia.max_score) + ". You did not pass.")
    else:
        labelScore.config(text="The score is: " + str(trivia.score) + " out of " + str(trivia.max_score))
    
    print("The score is:" + str(trivia.score))

#Configuration for the scrollbar
def scroll_config(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=300) 

def get_grade():
    return grade

#A callback function for the score menues
def scoreMenu_callback0(guess, gradeMenue0answer, menu):
    print ("------------callback0-----guess:" + str(guess) + " answer:" +  gradeMenue0answer)
    if (str(guess).strip() == str(gradeMenue0answer).strip()):
        trivia.score = trivia.score + trivia.score_index
        print( trivia.score)
    #Disable selected menu
    menu.config(state="disabled")
    
#Reload for each grade selected
def gradeMenu_callback(self, item, frame, controller):
    print("value is:" + str(item))
    grade = item
    #trivia = get_trivia(grade)
    #clear the score
    print("The score is:" + str(trivia.score))
    trivia.score = 0
    
    finalList = trivia.readFile(file_name, grade)
    #apply the random to shuffle the list
    shuffled = random.shuffle(finalList)
    print(finalList)
    
    #clear the grid
    for widget in frame.winfo_children():
        widget.destroy()
    
    canvas=Canvas(frame)

    form=Frame(canvas)
    
    for widget in form.winfo_children():
        widget.destroy() 
    
    scrollbar = Scrollbar(frame, orient="vertical",command=canvas.yview)

    scrollbar.pack(side = "right", fill = "y" )        

    canvas.pack(side="top")

    canvas.create_window((0,0),window=form,anchor='nw')        
    canvas.configure(yscrollcommand=scrollbar.set)        

    #Due to TKINTER LIMITATIONS to send a control name / index to the callback method
    #added the following static fields to display Questions / Answers
    tk_grade_var0 = tk.StringVar(self)
    data0 = {'True','False'}
    tk_grade_var0.set('Select') #set the default option
                
    arr= finalList[0]
    menue0 = tk.Frame(form)
    menue0.pack(side="top", fill="both") 
    label = tk.Label(menue0, text=" " + arr[0])
    label.pack(side="left", anchor="nw", pady="10")          
    gradeMenue0 = tk.OptionMenu(menue0, tk_grade_var0, *sorted(data0),  command=lambda item=tk_grade_var0: scoreMenu_callback0(item, arr[1], gradeMenue0))
    gradeMenue0.pack(side="right", anchor="e") 
 
       
    tk_grade_var1 = tk.StringVar(self)
    data1 = {'True','False'}
    tk_grade_var1.set('Select') #set the default option
        
    arr1= finalList[1]
    menue1 = tk.Frame(form)
    menue1.pack(side="top", fill="both")
    label1 = tk.Label(menue1, text=" " + arr1[0])
    label1.pack(side="left", anchor="nw", pady="10")          
    gradeMenue1 = tk.OptionMenu(menue1, tk_grade_var1, *sorted(data1),  command=lambda item=tk_grade_var1: scoreMenu_callback0(item, arr1[1], gradeMenue1))
    gradeMenue1.pack(side="right", anchor="w")         
            

    tk_grade_var2 = tk.StringVar(self)
    data2 = {'True','False'}
    tk_grade_var2.set('Select') #set the default option
        
    arr2= finalList[2]
    menue2 = tk.Frame(form)
    menue2.pack(side="top", fill="both") 
    label2 = tk.Label(menue2, text=" " + arr2[0])
    label2.pack(side="left", anchor="nw", pady="10")          
    gradeMenue2 = tk.OptionMenu(menue2, tk_grade_var2, *sorted(data2),  command=lambda item=tk_grade_var2: scoreMenu_callback0(item, arr2[1], gradeMenue2))
    gradeMenue2.pack(side="right", anchor="w")   
 
    tk_grade_var3 = tk.StringVar(self)
    data3 = {'True','False'}
    tk_grade_var3.set('Select') #set the default option

    arr3= finalList[3]
    menue3 = tk.Frame(form)
    menue3.pack(side="top", fill="both") 
    label3 = tk.Label(menue3, text=" " + arr3[0])
    label3.pack(side="left", anchor="nw", pady="10")          
    grademenue3 = tk.OptionMenu(menue3, tk_grade_var3, *sorted(data3),  command=lambda item=tk_grade_var3: scoreMenu_callback0(item, arr3[1], grademenue3))
    grademenue3.pack(side="right", anchor="w")
    
    tk_grade_var4 = tk.StringVar(self)
    data4 = {'True','False'}
    tk_grade_var4.set('Select') #set the default option

    arr4= finalList[4]
    menue4 = tk.Frame(form)
    menue4.pack(side="top", fill="both") 
    label4 = tk.Label(menue4, text=" " + arr4[0])
    label4.pack(side="left", anchor="nw", pady="10")          
    grademenue4 = tk.OptionMenu(menue4, tk_grade_var4, *sorted(data4),  command=lambda item=tk_grade_var4: scoreMenu_callback0(item, arr4[1], grademenue4))
    grademenue4.pack(side="right", anchor="w")

    tk_grade_var5 = tk.StringVar(self)
    data5 = {'True','False'}
    tk_grade_var5.set('Select') #set the default option

    arr5= finalList[5]
    menue5 = tk.Frame(form)
    menue5.pack(side="top", fill="both") 
    label5 = tk.Label(menue5, text=" " + arr5[0])
    label5.pack(side="left", anchor="nw", pady="10")          
    grademenue5 = tk.OptionMenu(menue5, tk_grade_var5, *sorted(data5),  command=lambda item=tk_grade_var5: scoreMenu_callback0(item, arr5[1], grademenue5))
    grademenue5.pack(side="right", anchor="w")
    
    tk_grade_var6 = tk.StringVar(self)
    data6 = {'True','False'}
    tk_grade_var6.set('Select') #set the default option

    arr6= finalList[6]
    menue6 = tk.Frame(form)
    menue6.pack(side="top", fill="both") 
    label6 = tk.Label(menue6, text=" " + arr6[0])
    label6.pack(side="left", anchor="nw", pady="10")          
    grademenue6 = tk.OptionMenu(menue6, tk_grade_var6, *sorted(data6),  command=lambda item=tk_grade_var6: scoreMenu_callback0(item, arr6[1], grademenue6))
    grademenue6.pack(side="right", anchor="w")    

    tk_grade_var7 = tk.StringVar(self)
    data7 = {'True','False'}
    tk_grade_var7.set('Select') #set the default option

    arr7= finalList[7]
    menue7 = tk.Frame(form)
    menue7.pack(side="top", fill="both") 
    label7 = tk.Label(menue7, text=" " + arr7[0])
    label7.pack(side="left", anchor="nw", pady="10")          
    grademenue7 = tk.OptionMenu(menue7, tk_grade_var7, *sorted(data7),  command=lambda item=tk_grade_var7: scoreMenu_callback0(item, arr7[1], grademenue7))
    grademenue7.pack(side="right", anchor="w")

    tk_grade_var8 = tk.StringVar(self)
    data8 = {'True','False'}
    tk_grade_var8.set('Select') #set the default option

    arr8= finalList[8]
    menue8 = tk.Frame(form)
    menue8.pack(side="top", fill="both") 
    label8 = tk.Label(menue8, text=" " + arr8[0])
    label8.pack(side="left", anchor="nw", pady="10")          
    grademenue8 = tk.OptionMenu(menue8, tk_grade_var8, *sorted(data8),  command=lambda item=tk_grade_var8: scoreMenu_callback0(item, arr8[1], grademenue8))
    grademenue8.pack(side="right", anchor="w")
    
    tk_grade_var9 = tk.StringVar(self)
    data9 = {'True','False'}
    tk_grade_var9.set('Select') #set the default option

    arr9= finalList[9]
    menue9 = tk.Frame(form)
    menue9.pack(side="top", fill="both") 
    label9 = tk.Label(menue9, text=" " + arr9[0])
    label9.pack(side="left", anchor="nw", pady="10")          
    grademenue9 = tk.OptionMenu(menue9, tk_grade_var9, *sorted(data9),  command=lambda item=tk_grade_var9: scoreMenu_callback0(item, arr9[1], grademenue9))
    grademenue9.pack(side="right", anchor="w")
    
    form.bind("<Configure>", lambda event, canvas=canvas: scroll_config(event, canvas))
    
def get_trivia(grade):
    trivia = Trivia(int(grade))
    return trivia

class ChemGUI(tk.Frame):
    print("----------------init--------------")  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #grade = 10
        #trivia = Trivia(int(grade))
        
        label = tk.Label(self, text="Chemistry Trivia Game",font = "Helvetica 12 bold italic")
        label.pack(side="top", fill="x", pady=10)
        
        header = tk.Frame(self)
        header.pack(side="top", fill="both")
        
        label = tk.Label(header, text="\t\t\t\tPlease select your grade.")
        label.pack(side="left", fill="x", anchor="e", pady=10)        
        
        
        spacer = tk.Label(header, text="\t\t\t\t")
        spacer.pack(side="right", anchor="w")
        
        tk_grade_var = tk.StringVar(self)
        data = {'9','10','11','12'}
        tk_grade_var.set('9') #set the default option
          
        gradeMenu = tk.OptionMenu(header, tk_grade_var, *sorted(data), command=lambda item=tk_grade_var: gradeMenu_callback(self, item, frame, controller))
        gradeMenu.pack(side="right", anchor="w") 
        
        #Questions
        
        print('Starting the trivia program.')
        #grade = input('Please enter your grade:')
        grade = get_grade()
        
        print("grade " + str(grade))
       
        #Read the file and load the corresponding
        #array
        
        finalList = trivia.readFile(file_name, grade)
        #apply the random to shuffle the list
        #shuffled = random.shuffle(finalList) 
        print("finalList: " + str(finalList))
        
        frame=tk.Frame(self)
        frame.pack(side="top", fill="both")
        
        canvas=Canvas(frame)
        form=Frame(canvas)
        scrollbar = Scrollbar(frame, orient="vertical",command=canvas.yview)
        scrollbar.pack(side = "right", fill = "y" )        
        canvas.pack(side="top")
        
        canvas.create_window((0,0),window=form,anchor='nw')        
        canvas.configure(yscrollcommand=scrollbar.set)        

        #Due to TKINTER LIMITATIONS to send a control name / index to the callback method
        #added the following static fields to display Questions / Answers
        tk_grade_var0 = tk.StringVar(self)
        data0 = {'True','False'}
        tk_grade_var0.set('Select') #set the default option
                
        arr= finalList[0]
        menue0 = tk.Frame(form)
        menue0.pack(side="top", fill="both") 
        label = tk.Label(menue0, text=" " + arr[0])
        label.pack(side="left", anchor="nw", pady="10")          
        gradeMenue0 = tk.OptionMenu(menue0, tk_grade_var0, *sorted(data0),  command=lambda item=tk_grade_var0: scoreMenu_callback0(item, arr[1], gradeMenue0))
        gradeMenue0.pack(side="right", anchor="e") 
 
       
        tk_grade_var1 = tk.StringVar(self)
        data1 = {'True','False'}
        tk_grade_var1.set('Select') #set the default option
        
        arr1= finalList[1]
        menue1 = tk.Frame(form)
        menue1.pack(side="top", fill="both")
        label1 = tk.Label(menue1, text=" " + arr1[0])
        label1.pack(side="left", anchor="nw", pady="10")          
        gradeMenue1 = tk.OptionMenu(menue1, tk_grade_var1, *sorted(data1),  command=lambda item=tk_grade_var1: scoreMenu_callback0(item, arr1[1], gradeMenue1))
        gradeMenue1.pack(side="right", anchor="w")         
            

        tk_grade_var2 = tk.StringVar(self)
        data2 = {'True','False'}
        tk_grade_var2.set('Select') #set the default option
        
        arr2= finalList[2]
        menue2 = tk.Frame(form)
        menue2.pack(side="top", fill="both") 
        label2 = tk.Label(menue2, text=" " + arr2[0])
        label2.pack(side="left", anchor="nw", pady="10")          
        gradeMenue2 = tk.OptionMenu(menue2, tk_grade_var2, *sorted(data2),  command=lambda item=tk_grade_var2: scoreMenu_callback0(item, arr2[1], gradeMenue2))
        gradeMenue2.pack(side="right", anchor="w")
        
        tk_grade_var3 = tk.StringVar(self)
        data3 = {'True','False'}
        tk_grade_var3.set('Select') #set the default option
    
        arr3= finalList[3]
        menue3 = tk.Frame(form)
        menue3.pack(side="top", fill="both") 
        label3 = tk.Label(menue3, text=" " + arr3[0])
        label3.pack(side="left", anchor="nw", pady="10")          
        grademenue3 = tk.OptionMenu(menue3, tk_grade_var3, *sorted(data3),  command=lambda item=tk_grade_var3: scoreMenu_callback0(item, arr3[1], grademenue3))
        grademenue3.pack(side="right", anchor="w")
        
        tk_grade_var4 = tk.StringVar(self)
        data4 = {'True','False'}
        tk_grade_var4.set('Select') #set the default option
    
        arr4= finalList[4]
        menue4 = tk.Frame(form)
        menue4.pack(side="top", fill="both") 
        label4 = tk.Label(menue4, text=" " + arr4[0])
        label4.pack(side="left", anchor="nw", pady="10")          
        grademenue4 = tk.OptionMenu(menue4, tk_grade_var4, *sorted(data4),  command=lambda item=tk_grade_var4: scoreMenu_callback0(item, arr4[1], grademenue4))
        grademenue4.pack(side="right", anchor="w")

        tk_grade_var5 = tk.StringVar(self)
        data5 = {'True','False'}
        tk_grade_var5.set('Select') #set the default option
    
        arr5= finalList[5]
        menue5 = tk.Frame(form)
        menue5.pack(side="top", fill="both") 
        label5 = tk.Label(menue5, text=" " + arr5[0])
        label5.pack(side="left", anchor="nw", pady="10")          
        grademenue5 = tk.OptionMenu(menue5, tk_grade_var5, *sorted(data5),  command=lambda item=tk_grade_var5: scoreMenu_callback0(item, arr5[1], grademenue5))
        grademenue5.pack(side="right", anchor="w")
        
        tk_grade_var6 = tk.StringVar(self)
        data6 = {'True','False'}
        tk_grade_var6.set('Select') #set the default option
    
        arr6= finalList[6]
        menue6 = tk.Frame(form)
        menue6.pack(side="top", fill="both") 
        label6 = tk.Label(menue6, text=" " + arr6[0])
        label6.pack(side="left", anchor="nw", pady="10")          
        grademenue6 = tk.OptionMenu(menue6, tk_grade_var6, *sorted(data6),  command=lambda item=tk_grade_var6: scoreMenu_callback0(item, arr6[1], grademenue6))
        grademenue6.pack(side="right", anchor="w")        

        tk_grade_var7 = tk.StringVar(self)
        data7 = {'True','False'}
        tk_grade_var7.set('Select') #set the default option
    
        arr7= finalList[7]
        menue7 = tk.Frame(form)
        menue7.pack(side="top", fill="both") 
        label7 = tk.Label(menue7, text=" " + arr7[0])
        label7.pack(side="left", anchor="nw", pady="10")          
        grademenue7 = tk.OptionMenu(menue7, tk_grade_var7, *sorted(data7),  command=lambda item=tk_grade_var7: scoreMenu_callback0(item, arr7[1], grademenue7))
        grademenue7.pack(side="right", anchor="w")
 
        tk_grade_var8 = tk.StringVar(self)
        data8 = {'True','False'}
        tk_grade_var8.set('Select') #set the default option
    
        arr8= finalList[8]
        menue8 = tk.Frame(form)
        menue8.pack(side="top", fill="both") 
        label8 = tk.Label(menue8, text=" " + arr8[0])
        label8.pack(side="left", anchor="nw", pady="10")          
        grademenue8 = tk.OptionMenu(menue8, tk_grade_var8, *sorted(data8),  command=lambda item=tk_grade_var8: scoreMenu_callback0(item, arr8[1], grademenue8))
        grademenue8.pack(side="right", anchor="w")
        
        tk_grade_var9 = tk.StringVar(self)
        data9 = {'True','False'}
        tk_grade_var9.set('Select') #set the default option
    
        arr9= finalList[9]
        menue9 = tk.Frame(form)
        menue9.pack(side="top", fill="both") 
        label9 = tk.Label(menue9, text=" " + arr9[0])
        label9.pack(side="left", anchor="nw", pady="10")          
        grademenue9 = tk.OptionMenu(menue9, tk_grade_var9, *sorted(data9),  command=lambda item=tk_grade_var9: scoreMenu_callback0(item, arr9[1], grademenue9))
        grademenue9.pack(side="right", anchor="w")
        
        form.bind("<Configure>", lambda event, canvas=canvas: scroll_config(event, canvas))
    
        ''' Initial loop implimentation
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
        '''
        #eof Questions

        labelScore = tk.Label(self, text=" Please make your selection!",font = "Helvetica 12 bold italic")
        labelScore.pack(side="left", fill="x", pady=10) 
        
        score_button = tk.Button(self, text="Check Score", command = lambda:check_score(labelScore))
        score_button.config( height = 2, width = 20 )
        score_button.pack()  
        
        restart_button = tk.Button(self, text="Return to the main screen", command=self.restart)
        restart_button.config( height = 2, width = 20 )
        restart_button.pack()
     
    def restart(self):
        #self.refresh()
        self.controller.show_frame("InitPage")    
        