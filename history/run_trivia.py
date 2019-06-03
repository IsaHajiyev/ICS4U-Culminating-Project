from Trivia import*

print('Starting the trivia program.')

grade = input('Please enter your grade:')

file_name="history_questions.txt"
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

#Iterate over the result array
for x, y in zip(trivia.questList, trivia.answList):
    
    ans = str(input(x + ' ')).upper()
    
    if not(ans == 'A' or ans == 'B' or ans == 'C'):
        print('Invalid answer, the answer should be A, B or C')
    
    if (ans == y):
        score = score + points
        #print(x + "  " +  y + "   " + str(score))

#Using If else statement to display the final greeting
if (score == len(trivia.questList) * points):
    print('Congratulations! You\'ve just scored ' + str(score) + ' points out of ' + str(len(trivia.questList) * points) + '.') 
else:
    print('Thank you. Your score is ' + str(score) + ' points out of ' + str(len(trivia.questList) * points) + '.')