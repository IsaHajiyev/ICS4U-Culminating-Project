class Trivia():
    #constructor
    def __init__(self, s):
        self.grade = s
        
    #read file method    
    def readFile(self, file_name):
        #Reading the file
        #print("READING THE File: " + file_name)
        self.gradeList = []
        self.questList = []
        self.answList  = []
        
        # Open file for read (using loops, if statement).
        # Save content to arrays.
        with open(file_name, 'r') as file:
            for line in file:
                line = str(line).rstrip()
                cols = line.split('|')
                grade = int(str(cols[0]).split('_')[1])
                self.gradeList.append(grade)
                
                
                if (self.grade == grade):                    
                    #print('grade ' + str(grade))
                    self.questList.append(cols[1])
                    self.answList.append(cols[2])
        file.close()        
        