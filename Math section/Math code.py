class Trivia():
    #constructor
    def __init__(self, s):
        self.section = s
        
    #read file method    
    def readFile(self, file_name):
        #Reading the file
        #print("READING THE File: " + file_name)
        self.sectionList = []
        self.questList = []
        self.answList  = []
        
        # Open file for read (using loops, if statement).
        # Save content to arrays.
        with open(file_name, 'r') as file:
            for line in file:
                line = str(line).rstrip()
                cols = line.split('|')
                section = str(cols[0])
                self.sectionList.append(section)
                
                
                if (self.section == section):                    
                    #print('grade ' + str(grade))
                    self.questList.append(cols[1])
                    self.answList.append(cols[2])
        file.close()   
#from Trivia import*

print('Starting the trivia program.')

section = str(input('Please enter the section: functions, x and y intercepts or sin,cos,tan ratios: '))

file_name="math changes.txt"
points = 2
score = 0
#Lowercasing user input so uppercase does not affect the program
section = section.lower()
#variables for each section
func = "functions"
intercepts = "x and y intercepts"
ratios = "sin,cos,tan ratios"
#Call the class constructor.
trivia = Trivia(section)

#Read the file and load the corresponding
#array
trivia.readFile(file_name)

#Error message if section is not the same
if not section in trivia.sectionList:
    print('Section is not supported, please type in a section exactly as written above or remove any spaces.')
    exit()
#Creating a prompt based on section chosen
elif section == func:
    print('Please provide your answer in A or B/A, B or C format')
elif section == intercepts:
    print('Please provide your answer in (0,0) format')
elif section == ratios:
    print('Please provide your answer in as a number according to what the question asks')
#Iterate over the result array
for x, y in zip(trivia.questList, trivia.answList):
        
    ans = str(input(x + ' ')).upper()
        
    #if not(ans == 'A' or ans == 'B' or ans == 'C'):
        #print('Invalid answer, the answer should be A, B or C')
        
    if (ans.lower() == y):
        score = score + points
        #print(x + "  " +  y + "   " + str(score))  

#Using If else statement to display the final greeting
if (score == len(trivia.questList) * points):
    print('Congratulations! You\'ve just scored ' + str(score) + ' points out of ' + str(len(trivia.questList) * points) + '.') 
else:
    print('Thank you. Your score is ' + str(score) + ' points out of ' + str(len(trivia.questList) * points) + '.')