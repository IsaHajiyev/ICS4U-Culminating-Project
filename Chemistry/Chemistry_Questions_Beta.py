import sys
from random import shuffle

grade_11_chem_question_list = [ # tuple of the form (question, dict of answers), 16 questions currently
    ('Which of these represent chemical change?',
    {'Bubbling': True, 'Melting': False, 'Evaporating': False, 'Dissolving': False}),
    
    ('Which of these represent physical change?',
    {'Fizzing': False, 'Oxidation': False, 'Freezing': True, 'Foaming': False}),
    
    ('What are substances that undergo reaction called?',
    {'Products': False, 'Resolutions': False, 'Synthesis': False, 'Reactants': True}),      
    
    ('The Law of Conservation of Mass states that:',
    {'Matter cannot be created or destroyed during a chemical reaction': True, 'No energy is consumed during reactions': False, 'All energy is used up in a reaction': False, 'Matter is created or destroyed during a chemical reaction': False}),
    
    ('Which of the below represents Synthesis Reactions?',
    {'AB -> A + B': False, 'A + B -> AB': True, ' A + AB -> BAA': False, 'AB -> AB + C': False}),  
    
    ('In a decomposition reaction, the lone reactant breaks...',
    {'up into smaller molecules': True, 'up into smaller products': False, 'up into greater atoms': False, 'None of the Above': False}),  
    
    ('Which of the following is not a Diatomic Molecule?',
    {'H2': False, 'F2': False, 'Br2': False, 'ClO2': True}),  
    
    ('In a double displacement reaction:',
    {'atoms are static between two reactants': False, 'atoms are exchanged between two reactants': True, 'atoms are removed between two products': False, 'atoms are gained between two products': False}),  
    
    ('___ is the substance that dissolves in a solvent to form a solution',
    {'Solvent': False, 'Solution': False, 'Solubility': False, 'Solute': True}),  
    
    ('___ is the medium in which a solute dissolves',
    {'Solvent': True, 'Solution': False, 'Solute': False, 'Aqueous': False}),  
    
    ('What is the numerical value for a mole',
    {'4.05 x 10^13': False, '6.02 x 10^23': True, '2.10 x 10^53': False, '2.36 x 10^-13': False}),  
    
    ('What best describes Stoichiometry?',
    {'The amount of reactants involved in chemical reactions.': False, 'The amount of products involved in chemical reactions.': False, 'he study of the amount of reactants and products involved in physical reactions.': False, 'None of the Above': True}),
    
    ('What is the Limiting Reagent?',
    {'the reageant you run out of last': False, 'the reagent present in the greatest stoichiometric amount': False, 'the reagent present in the smallest stoichiometric amount': True, 'None of the Above': False}), 
    
    ('When water is a solvent, the solution is',
    {'gaseous': False, 'aqueous': True, 'liquid': False, 'solid': False}),  
    
    ('Binary Compounds:',
    {'consist of two types of diatomic ions': False, 'consist of two types of triatomic ions': False, 'consist of two types of pentatomic ions': False, 'consist of two types of monatomic ions': True}),  
    
    ('Which is not a prefix used when naming Hydrated Compounds?',
    {'tri': False, 'penta': False, 'decta': True, 'mono': False}),     

]

grade_12_chem_question_list = [# tuple of the form (question, dict of answers), 17 questions currently
    ('What is Calorimetry used for?',
    {'Exchange Heat': False, 'Increase Heat': False, 'Remove Heat': False, 'Measure Heat Transfer': True}),

    ('What is the formula used to calculate transferred heat?',
    {'Q/MCdeltaT': False, 'MC/QdeltaT': False, 'deltaT/Qmc': False, 'QmcdeltaT': True}),

    ('What is a Calorimeter?',
    {'A device which checks temperature': False, 'Checks type of element': False,  'Releases Energy': False, 'Measures Heat': True}),

    ('What is Thermochemistry?',
    {'Study of Chemicals': False, 'Study of Reactions': False, 'Study of Chemistry': False, 'Study of Heat Energy': True}),
    
    ('How many ways are there to calculate Hess\'s Law?',
    {'One': False, 'Two': True, 'Three': False, 'None': False}),
    
    ('What is the total energy change from Hess\'s law dependent on?',
    {'Initial and Final Stages': True, 'Intermedium Stages': False, 'Reaction Route': False, 'Final Stages': False}),
    
    ('How many factors modify rate of chemical reaction?',
    {'Three': False, 'Four': False, 'Seven': False, 'Five': True}),
    
    ('Which of these factors is NOT a factor that modifies the rate of chemical reaction?',
    {'Temperature': False, 'Speed': True, 'Pressure': False, 'Presence of a Catalyst': False, 'Concentration of Reactants': False}),
    
    ('Which is a requirement for Equilibrium?',
    {'Constant Temperature and External Pressure': True, 'Static Pressure': False, 'Static Temperature': False, 'Constant Addition of Substances': False}),
    
    ('What is the equation for Reaction Quotient?',
    {'Products * Reactants': False, 'Reactants + Products': False, 'Products/Reactants': True, ' Products - Reactants': False}),
    
    ('What does Boyle\'s Law state?',
    {'As pressure increases, volume increases.': False, 'As volume decreases, pressure decreases.': False, 'As pressure increases, volume decreases': True, 'None of the Above': False}),
    
    ('The Law of Equilibrium states that:',
    {'K cannot be 0 or under': True, 'The value of K can be found without experimentation': False, 'A large value of K prefers reactants at equilibrium': False, 'A small value of K prefers products at equilibrium': False}),
    
    ('Which state of matter is not included in the K calculation?',
    {'Gas': False, 'Liquid': False, 'Plasma': False, 'Solid': True}),
    
    ('Which is true about Acids?',
    {'They are always liquid': False, 'They can never react with carbonates': False, 'They have a bitter taste': False, 'They react with metal to produce hydrogen gas': True}),
    
    ('Which is false about Bases?',
    {'They can be liquid or solid': False, 'They do not react with metals to make hydrogen gas': False, 'They are terrible conductors of electricity': True, 'Dissolves in water to produce hydroxide ions': False}),
    
    ('Primary Batteries:',
    {'cannot be recharged': True, 'can be used multiple times without recharge': False, 'are single-use because of their size': False, 'are rechargable': False}),
    
    ('Corrosion occurs when',
    {'exposed to water': False, 'exposed to carbon': False, 'exposed to oxygen': False, 'exposed to oxygen and water': True}),    
]

def get_input_in_list_1(lst): #Grade 11
    while True:
        print("Please type the correct answer (Case Sensitive): \n" + "  \n".join(lst))
        user_input = input("")
        if user_input in lst: #Examines if the answer typed matches the dictionary
            return user_input

def get_input_in_list_2(lst): #Grade 12
    while True:
        print("Please type the correct answer (Case Sensitive): \n" + "  \n".join(lst))
        user_input = input("")
        if user_input in lst: #Examines if the answer typed matches the dictionary
            return user_input

def questions():
    wrong = 0 #Incorrect answers
    right = 0 #Correct answers
    score = 0 #Score System
    streak = 0 #Calculates the number of correct answers in a row
    question_tracker = 0 #Tracks how many questions have passed
    grade_11_q = 0 #Sees if grade 11 test is active
    grade_12_q = 0 #Sees if grade 12 test is active
    
    user_input = "Welcome to the trivia quiz for Chemistry. Please type below what grade you wish to try (Grade 11 or 12) or quit to exit the game \n"
    
    while(user_input != "quit"):
        n = input(user_input)
        if (n == "quit"):
            sys.exit()
        
        if n == "Grade 11":
            print('Selecting Grade 11 questions... \n')
            grade_11_q = 1
            while grade_11_q == 1:
            
                for each_question, answer_dict in grade_11_chem_question_list:
                    answers = list(answer_dict)
                    shuffle(answers) #Shuffles the answers randomly
                    print(each_question)
                    n = get_input_in_list_1(answers)
                    
                    if question_tracker == 16 or question_tracker == 33: #Determines if this is a first game or not
                        print('You have finished the Grade 11 Quiz. Would you like to try again? Type \'yes\' if so.')
                        if (n == "yes" or n == "Yes"): #Restarts the game from scratch
                            print("Your stats have been reset.")
                            wrong = 0
                            right = 0
                            score = 0
                            streak = 0
                            grade_11_q = 0
                            continue
                        else: #Exits the game
                            print("Thank you for playing.")
                            sys.exit()                
    
                    if answer_dict[n]:
                        print('Your answer is correct!\n')
                        right += 1
                        score += 1
                        streak += 1
                        question_tracker += 1
                        if streak >= 2:
                            score += streak #Increases the score by the amount of correct answers in a row
                    else:
                        print('Your answer is false!\n')
                        wrong += 1
                        score -= 1
                        streak = 0
                        question_tracker += 1
                    #Helps user keep track of current scores
                    print('So far, you answered {0} questions correctly and {1} incorrectly.'.format(right, wrong))
                    print('Your current score is', score)
                    print('You have answered', streak,'question(s) correctly in a row! Keep it up! \n')
        
        elif n == "Grade 12":
            print('Selecting Grade 11 questions... \n')
            grade_12_q = 1
            while grade_12_q == 1:            

                for each_question, answer_dict in grade_12_chem_question_list:
                    answers = list(answer_dict)
                    shuffle(answers) #Shuffles the answers randomly
                    print(each_question)
                    n = get_input_in_list_2(answers)
                    
                    if question_tracker == 17 or question_tracker == 33: #Determines if this is a first game or not
                        print('You have finished the Grade 12 Quiz. Would you like to try again? Type \'yes\' if so.')
                        
                        if (n == "yes" or n == "Yes"): #Restarts the game from scratch
                            print("Your stats have been reset.")
                            wrong = 0
                            right = 0
                            score = 0
                            streak = 0
                            grade_12_q = 0
                            continue
                        else: #Exits the game
                            print("Thank you for playing.")
                            sys.exit()
            
                    if answer_dict[n]:
                        print('Your answer is correct!\n')
                        right += 1
                        score += 1
                        streak += 1
                        question_tracker += 1
                        if streak >= 2:
                            score += streak #Increases the score by the amount of correct answers in a row
                    else:
                        print('Your answer is false!\n')
                        wrong += 1
                        score -= 1
                        streak = 0
                        question_tracker += 1
                    #Helps user keep track of current scores
                    print('So far, you answered {0} questions correctly and {1} incorrectly.'.format(right, wrong))
                    print('Your current score is', score)
                    print('You have answered', streak,'question(s) correctly in a row! Keep it up! \n')
                
        else:
            print("Please type Grade 11 or Grade 12, or type quit to exit the game")


if __name__ == '__main__':
    questions()