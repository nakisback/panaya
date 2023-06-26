# namePicker.py
# Picks an inputted amount of random names from a CSV file.
# namePicker.py G2-1.xlsx 6 questions
# namePicker.py G2-1.xlsx 5 questions skipCd
# namePicker.py G2-1.xlsx 3 books - Picks 3 boys and 3 girls to pass books out

#TODO: Reformat the list to call on a different student for a specific question
#TODO: Prompts user to fill out what they missed.
#TODO: Prompts user for another round (at the end of questionAllocator)
#TODO: (30/5/23): Look up countdown fonts on https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#TODO: (3/6/23): Print out the current RSD% average for a specific quiz or range of quizzes
#TODO: (3/6/23): ^Apply this to all classes
#TODO: (19/6/23): Make Student model
#TODO: (20/6/23): Make statistics program
#TODO: (26/6): Make assigning group names optional
# Did this get saved?

#IDEAS:
# 1. <to be> question maker -- Picks a random student, picks a random topic

import os, sys, random, time, csv, shutil
import callers

script_dir = os.path.dirname('namePicker.py')
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

OPTIONS = {('1', 'QUESTIONS'): 'questions',
           ('2', 'BOOKS'): 'passing out books',
           ('3', 'BROOMS'): 'sweeping',
           ('4', 'VOLUNTEERS'): 'doing whatever is needed',
           ('5', 'GROUPS'): 'dividing class into groups',
           ('6', 'JEOPARDY'): 'playing Jeopardy',
           ('7', 'PRINT'): '<<TODO: printing student info>>',
           ('8', 'RESET'): '<<TODO: resetting student counts>>'}
CLASSES = ['1', '2', '3', '4', '5']
FILENAME = ''
HEIGHT = shutil.get_terminal_size()[1]

def main():
    #print('\n' * HEIGHT)
    #print('HEIGHT: ' + str(HEIGHT))
    os.system('cls')

    students = []
    # User inputs everything one-by-one
    if len(sys.argv) <= 1:

        while True:
            # input class
            while True:
                response = input('Class: ')
                if response[-1] in CLASSES:
                    FILENAME = 'G2-' + response[-1] + '.csv'
                    path = os.path.join(__location__, FILENAME)
##                    print('path: ', end='')
##                    print(path)
##                    print('location: ', end='')
##                    print(__location__)
##                    print('file: ', end='')
##                    print(__file__)
##                    print('os.path.dirname(__file__): ', end='')
##                    print(os.path.dirname(__file__))
##                    print('os.getcwd(): ', end='')
##                    print(os.getcwd())
                    with open(path, 'r', encoding='utf-8-sig') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            students.append(row)
                            #print(row)
                    print('\n')
                    break
                else:
                    print(f"Class {response} is not a class.")

            # input choice
            while True:
                choice = ''
                print('Please type in an option below:')
                for option in OPTIONS:
                    print(f'  {option[0]}. {option[1]} for {OPTIONS[option]}')
                response = input('>>> ')
                for option in OPTIONS:
                    # option is a key-value pair with the 'key' being a tuple
                    if str(response) == option[0] or str(response).upper() == option[1]:
                        #print(f'{response} is in {option}')
                        choice = option
                        print('\n')
                        break
                if choice != '':
                    #print(f'The choice is {choice}')
                    break
                else:
                    print(f'>>>{response} is not a valid response.\n')

            # input number of students
            while True:
                if choice[1] == 'JEOPARDY':
                    prompt = 'Number of Questions: '
                elif choice[1] == 'GROUPS':
                    prompt = 'Number of Groups: '
                else:
                    prompt = 'Number of Students: '
                #callers.spongebobMaker()
                response = input(prompt)
                if response.isnumeric() == True and int(response) > 0:
                    num = int(response)
                    print('\n')
                    break
                else:
                    print(f"{response} is not a proper input.")
            break

        try:
            if choice[1] == 'QUESTIONS':
                callers.questionAllocator(path, students, num)
            elif choice[1] in ['BOOKS', 'BROOMS', 'VOLUNTEERS']:
                callers.bookPasser(path, students, num, choice[1], OPTIONS[choice])
            elif choice[1] == 'JEOPARDY':
                callers.groupQuestions(path, students, num)
            elif choice[1] == 'GROUPS':
                groups = callers.groupsMaker(students, num)
        except ValueError:
            print("Student counts have not been assigned...")
            
    # User inputs everything in a single go
    # namePicker.py G2-1.csv 4
    # sys.argv[0] --> program
    # sys.argv[1] --> classname csv file
    # sys.argv[2] --> number of students
    # sys.argv[3] --> OPTIONAL: thing to do
    elif len(sys.argv) > 2:
        FILENAME = str(sys.argv[1])
        path = os.path.join(__location__, FILENAME)
        
        with open(path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
                #print(row)

        if sys.argv[2] == 'print':
            nicePrint(students)
            input('> ')
            sys.exit()
        
        num = int(sys.argv[2])
        #groupQuestions(students, num)
        
        if sys.argv[2] == 'print':
            nicePrint(students)
        
        # namePicker.py G2-1.csv 4
        if len(sys.argv) == 3:
            callers.questionAllocator(FILENAME, students, num)

        # 
        elif len(sys.argv) == 4:
            # namePicker.py G2-1.csv 5 groups
            # sys.argv[3] --> (e.g., 5) total number of questions 
            if sys.argv[3] == 'groups':
                callers.groupQuestions(students, num)
            else:
                # namePicker.py G2-1.csv 4 books
                if sys.argv[3] in OPTIONS:
                    thing = str(sys.argv[3])
                else:
                    thing = 'books'
                # TODO: needs working on
                callers.bookPasser(students, num, thing)

        

def nicePrint(List):
    for i in range(len(List)):
        print(str(i+1) + '. ', end='')
        print(List[i]['Name'] + ' -- ' + List[i]['Gender'])

def directoryInfo():
    
    __file__
    __location__
    return

#TODO: 
# Counts # per gender, # that haven't been called yet this round
#def classStats():
    


if __name__ == "__main__":
    #text = input('> ')
    main()


