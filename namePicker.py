# namePicker.py

#TODO: Prompts user for another round (at the end of questionAllocator)
#TODO: (30/5/23): Look up countdown fonts on https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#TODO: (3/6/23): Print out the current RSD% average for a specific quiz or range of quizzes
#TODO: (3/6/23): ^Apply this to all classes
#TODO: (20/6/23): Make statistics program
#TODO: (27/6): Make a standard time variable that can be switched on and off
#TODO: Make a list of valid inputs by user
#TODO: (2/8/23): Every "step" (i.e., things that require user input) should have 1 or 2 lines in between them
#TODO: (2/8/23): Implement a "Go Back" function
#TODO: (2/8/23): Pass a list to displayList or displayStudent and have it display the list one formatted line at a time

#TODO: Add jCount for jeopardy
#IDEAS:
# 1. <to be> question maker -- Picks a random student, picks a random topic

import os, sys, random, csv, shutil, display
import callers
from groups import groupsMaker

script_dir = os.path.dirname('namePicker.py')
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

OPTIONS = {('1', 'QUESTIONS'): 'questions',
           ('2', 'BOOKS'): 'passing out books',
           ('3', 'BROOMS'): 'sweeping',
           ('4', 'VOLUNTEERS'): 'doing whatever is needed',
           ('5', 'GROUPS'): 'dividing class into groups',
           ('6', 'JEOPARDY'): 'playing Jeopardy',
           ('7', 'TEST'): '<<TODO: printing student info>>',
           ('8', 'RESET'): '<<TODO: resetting student counts>>'}
CLASSES = ['1', '2', '3', '4', '5']
FILENAME = ''
HEIGHT = shutil.get_terminal_size()[1]

class Student:
    def __init__(self, id, studNum, name, gender, qCount, bCount, jCount):
        self.id = id
        self.studNum = studNum
        self.name = name
        self.gender = gender
        self.qCount = qCount
        self.bCount = bCount
        self.jCount = jCount

    def __str__(self):
        return f"(#{self.studNum}) {self.name}"
    
    def __repr__(self):
        return f"(#{self.studNum}) {self.name}"
        #return f"FROM __repr__ (#{self.studNum}) {self.name}"



def main():
    os.system('cls')

    students = []
    expStudentsList = []
    # User inputs everything one-by-one
    if len(sys.argv) <= 1:

        while True:
            # input class
            while True:
                response = input('Class: ')
                if response[-1] in CLASSES:
                    FILENAME = 'G2-' + response[-1] + '.csv'
                    path = os.path.join(__location__, FILENAME)
                    #printDirectoryInfo(path)
                    
                    with open(path, 'r', encoding='utf-8-sig') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            id = row['id']
                            studNum = row['#']
                            name = row['Name']
                            gender = row['Gender']
                            qCount = row['qCount']
                            bCount = row['bCount']
                            jCount = row['jCount']
                            student = Student(id, studNum, name, gender, qCount, bCount, jCount)
                            students.append(row)
                            expStudentsList.append(student)
                            #print(student)
                            #print(row)
                    print('\n')
                    break
                else:
                    print(f"Class {response} is not a class.")
            



            # input choice
            choice = display.optionsPrompt(OPTIONS)

            # input number of students
            while True:
                if choice[1] == 'JEOPARDY':
                    prompt = 'Number of Questions: '
                elif choice[1] == 'GROUPS':
                    break
                else:
                    prompt = 'Number of Students: '
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
                #callers.questionAllocator(path, students, num)
                callers.questionAllocator(path, expStudentsList, num)
            elif choice[1] in ['BOOKS', 'BROOMS', 'VOLUNTEERS']:
                #callers.bookPasser(path, students, num, choice[1], OPTIONS[choice])
                callers.bookPasser(path, expStudentsList, num, choice[1], OPTIONS[choice])
            elif choice[1] == 'JEOPARDY':
                #callers.groupQuestions(path, students, num)
                callers.groupQuestions(path, expStudentsList, num)
            # Fix this
            elif choice[1] == 'GROUPS':
                #groupsMaker(students)
                groupsMaker(expStudentsList)
            elif choice[1] == 'TEST':
                display.optionsPrompt('hello', options=OPTIONS)
        except ValueError:
            print("Student counts have not been assigned...")


def nicePrint(List):
    for i in range(len(List)):
        print(str(i+1) + '. ', end='')
        print(List[i]['Name'] + ' -- ' + List[i]['Gender'])

def printDirectoryInfo(path):
    print('path: ', end='')
    print(path)
    print('location: ', end='')
    print(__location__)
    print('file: ', end='')
    print(__file__)
    print('os.path.dirname(__file__): ', end='')
    print(os.path.dirname(__file__))
    print('os.getcwd(): ', end='')
    print(os.getcwd())
    return


if __name__ == "__main__":
    #text = input('> ')
    main()


