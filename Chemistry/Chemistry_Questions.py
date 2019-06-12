from random import shuffle

chem_question_list = [# tuple of the form (question, dict of answers), 15 questions currently
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
  
]

def get_input_in_list(lst):
    while True:
        print("Please type the correct answer (Case Sensitive): \n" + "  \n".join(lst))
        user_input = input("")
        if user_input in lst:
            return user_input

def questions():
    wrong = 0 #Incorrect answers
    right = 0 #Correct answers
    score = 0 #Score System
    streak = 0 #Calculates the number of correct answers in a row

    for each_question, answer_dict in chem_question_list:
        answers = list(answer_dict)
        shuffle(answers) #Shuffles the answers randomly
        print(each_question)
        user_answer = get_input_in_list(answers) 

        if answer_dict[user_answer]:
            print('Your answer is correct!\n')
            right += 1
            score += 1
            streak += 1
            if streak >= 2:
                score += streak #Increases the score by the amount of correct answers in a row
        else:
            print('Your answer is false!\n')
            wrong += 1
            score -= 1
            streak = 0
        print('So far, you answered {0} questions correctly and {1} incorrectly.'.format(right, wrong))
        print('Your current score is', score)
        print('You have answered', streak,'question(s) correctly in a row! Keep it up! \n')


if __name__ == '__main__':
    questions()