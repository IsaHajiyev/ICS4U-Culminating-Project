class Trivia():
    #constructor
    def __init__(self):
        self.grade = 0
        self.score = 0
        self.score_index = 2
        self.max_score = 20
        
    #read file method    
    def readFile(self, file_name, grade):
        #Reading the file
        #print("READING THE File: " + file_name)
        self.gradeList = []
        self.questList = []
        self.answList  = []
        
        self.grade = grade
        
        # Open file for read (using loops, if statement).
        # Save content to arrays.
        with open(file_name, 'r') as file:
            for line in file:
                line = str(line).rstrip()
                if (len(line) ==0):
                    continue
                cols = line.split('|')
                _grade = int(str(cols[0]).split('_')[1])
                self.gradeList.append(_grade)
                
                
                if (int(self.grade) == (_grade)):                    
                    #print('grade ' + str(grade))
                    self.questList.append(cols[1])
                    self.answList.append(cols[2])
        file.close()
        
        finalList = list(zip(self.questList, self.answList))

        return finalList 
        