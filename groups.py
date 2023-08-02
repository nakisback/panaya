#TODO: Make pairs, be able to select/repick

import random, time, display, os
from helpers import getNotCalledThisRound, getIndexFromID, getCallQueue

TIME_STANDARD = 1

class Group:
    def __init__(self, name):
        self.name = 'Group ' + str(name)
        self.roster = []
        self.callQueue = {}
        self.studentOrder = []

    def __str__(self):
        return f"{self.name}: {self.roster}"
    
class Groups:
    def __init__(self):
        self.order = []

'''class Student:
    def __init__(self, id, studNum, name, gender, qCount, bCount):
        self.id = id
        self.studNum = studNum
        self.name = name
        self.gender = gender
        self.qCount = qCount
        self.bCount = bCount'''



def groupsMaker(students):
    break_out_flag = False

    #print('groupsMaker')
    #print(students)

    '''print('groupsMaker')
    for student in students:
        print(student)'''
    
    # dividedBy: gender, odds/evens, sectioned, random, every nth student
    OPTIONS = {'1': 'GENDERS',
               '2': 'ODDS/EVENS',
               '3': 'SECTIONS',
               '4': 'RANDOM GROUPS',
               '5': 'EVERY NTH STUDENT'}

    groups = []

    prompt = "How should the groups be divided?"
    dividedBy = OPTIONS[display.optionsPrompt(OPTIONS, prompts=prompt)]

    print ('\n')
    if dividedBy == "GENDERS" or dividedBy == "ODDS/EVENS":
        numGroups = 2
    else:
        numGroups = int(input('How many groups are there? '))

    time.sleep(2 * TIME_STANDARD)
    print('\n')
    
    for i in range(numGroups):
        group = Group(str(i + 1))
        groups.append(group)

    # dividedBy: genders
    if dividedBy == 'GENDERS':
        groups[0].name = 'GIRLS Team'
        groups[1].name = 'BOYS Team'

        for student in students:
            if student.gender == 'boy':
                groups[1].roster.append(student)
            elif student.gender == 'girl':
                groups[0].roster.append(student)

    # dividedBy: odds/evens
    if dividedBy == 'ODDS/EVENS':
        groups[1].name = 'EVENS Team'
        groups[0].name = 'ODDS Team'
        for student in students:
            if (int(student.studNum) % 2) != 0:
                groups[0].roster.append(student)
            elif (int(student.studNum) % 2) == 0:
                groups[1].roster.append(student)

    # dividedBy: sections
    if dividedBy == 'SECTIONS':
        numPerSection = []
        groupInd = 0
        baseNumStud = len(students) // numGroups
        remNumStud = len(students) % numGroups

        for i in range(numGroups):
            numPerSection.append(baseNumStud)
            
        while True:
            i = 0
            if remNumStud != 0:
                numPerSection[i] += 1
                remNumStud -= 1
                i += 1
            else:
                break

        groupInd = 0
        for student in students:
            if len(groups[groupInd].roster) < numPerSection[groupInd]:
                groups[groupInd].roster.append(student)
            else:
                groupInd += 1
                groups[groupInd].roster.append(student)

        for group in groups:
            lowestStudNum = str(group.roster[0].studNum)
            highestStudNum = str(group.roster[-1].studNum)
            group.name += f" (#{lowestStudNum}-{highestStudNum})"
        
    # dividedBy: random groups
    if dividedBy == 'RANDOM GROUPS':
        while len(students) >= 1:
            if break_out_flag == True:
                break
            for i, group in enumerate(groups):
                randStud = random.choice(students)
                group.roster.append(randStud)
                #print(f"{randStud['Name']} is going to group {i+1}")
                students.pop(getIndexFromID(students, randStud.id))
                if len(students) == 0:
                    break_out_flag = True
                    break
    
    
    # dividedBy: every Nth student
    if dividedBy == 'EVERY NTH STUDENT':
        while True:
            i = 0
            for student in students:
                groups[i].roster.append(student)
                if i < len(groups) - 1:
                    i += 1
                else:
                    i = 0
            break


    display.displayGroups(groups)
        
    while True:
        print('Is there anything that needs to be changed? (Y/N)')
        response = input('>>> ')
        print()
        if response.upper().startswith('Y'):
            groups = editGroups(groups)
        elif response.upper().startswith('N'):
            os.system('cls')
            display.displayGroups(groups)
            break
    # Returns a list of dictionaries [{'name': '1', 'roster': [STUDENTS INFO, STUDENTS INFO]}, {'name': '1', 'roster': [STUDENTS INFO, STUDENTS INFO]}]
    for group in groups:
        group.callQueue = getCallQueue(group.roster, 'jCount')


    return groups

def editGroups(groups):
    EDIT_OPTIONS = {'1': 'changeGroupName',
                    '2': 'addStudent',
                    '3': 'removeStudent',
                    '4': 'moveStudent',
                    '5': 'shuffleStudents'}
    
    editedGroups = groups
    #print('This is editGroups()')
    
    prompt = "What would you like to do?"
    choice = EDIT_OPTIONS[display.optionsPrompt(EDIT_OPTIONS, prompts=prompt)]

    if choice == 'changeGroupName':
        editedGroups = changeGroupName(editedGroups)
    elif choice == 'addStudent':
        addStudent()
    elif choice == 'removeStudent':
        removeStudent(editedGroups)
    elif choice == 'moveStudent':
        editedGroups = moveStudent(groups)
    elif choice == 'shuffleStudents':
        editedGroups = shuffleStudents(editedGroups)

    return editedGroups

def changeGroupName(groups):
    targetGroup = None
    GROUP_NAMES = {}
    #print('This is changeGroupName')

    for i, group in enumerate(groups):
        GROUP_NAMES[str(i + 1)] = group.name
    prompt = "Which group needs its name changed?"
    choice = GROUP_NAMES[display.optionsPrompt(GROUP_NAMES, prompts=prompt)]
    print(GROUP_NAMES)
    print(choice)

    for i, group in enumerate(groups):
        if choice == group.name:
            targetGroup = group
            print(f"targetGroup's name is {targetGroup.name}")
            break

    newName = None
    while newName == None:
        hasDuplicate = False
        responseName = input(f"What should {targetGroup.name}'s new name be?\n>>>")
        print()
        
        for group in groups:
            if responseName.upper() == group.name.upper():
                hasDuplicate = True
                time.sleep(0.5 * TIME_STANDARD)
                print(f"There's already a group with the name \"{group.name}\".")
                time.sleep(0.5 * TIME_STANDARD)
                print(f"Please type in another name. . . \n")
        if hasDuplicate == False:
            newName = responseName

    targetGroup.name = newName

    return groups

def exists():
    return

# returns False if student can't be found
# should return group.name and group.roster[ind] index number/location
def findStudent(groups):
    targetStudent = None
    info = {'groupObj': None, 'groupName': '', 'indInGrp': ''}

    while targetStudent == None:
        responseStudentName = input("Which student? Enter their name or 4-digit id...\n>>> ")
        print()
        for group in groups:
            if targetStudent != None:
                break
            for i, student in enumerate(group.roster):
                if responseStudentName.upper() == student.name.upper():
                    targetStudent = student
                    info['groupObj'] = group
                    info['indInGrp'] = i
                    break
        if targetStudent == None:
            print("Could not find that student.")

    return info, targetStudent

def moveStudent(groups):
    info, targetStudent = findStudent(groups)
    oldGroup = info['groupObj']
    oldIndex = info['indInGrp']
    targetGroup = None

    while targetGroup == None:
        responseGroupName = input(f"Where do you want to move {targetStudent}? \n>>> ")     
        for group in groups:
            if responseGroupName.upper() == group.name.upper():
                targetGroup = group
                break
        if targetGroup == None:
            print(f"{responseGroupName} could not be found")
    targetGroup.roster.append(targetStudent)

    # Removes student at old index
    oldGroup.roster.pop(oldIndex)

    return groups

def addStudent():
    return


# 
def removeStudent(groups):
    info, targetStudent = findStudent(groups)
    targetGroup = info['groupObj']
    targetInd = info['indInGrp']

    #print(f"Removing {targetStudent.name} from {targetGroup.name} at ind {info['indInGrp']}")

    targetGroup.roster.pop(targetInd)
    print(f"Successfully removed {targetStudent} from {targetGroup.name}.")

    return

def shuffleStudents(groups):
    for group in groups:
        random.shuffle(group.roster)
    return groups