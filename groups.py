import random, time, display
from helpers import getNotCalled, generateNotCalled, getNotCalledThisRound, getIndexFromID

def groupsMaker(students):
    break_out_flag = False

    #print(students)
    
    # dividedBy: gender, odds/evens, sectioned, random, every nth student
    OPTIONS = {'1': 'GENDERS',
               '2': 'ODDS/EVENS',
               '3': 'SECTIONS',
               '4': 'RANDOM GROUPS',
               '5': 'EVERY NTH STUDENT'}
    
    #random.shuffle(students)
    groups = []

    print('How should the groups be divided?')
    while True:
        for key, value in OPTIONS.items():
            print("  %s. %s" % (key, value))

        response = input('>>> ')

        if response in OPTIONS:
            dividedBy = OPTIONS[response]
            break
        else:
            print('Incorrect input...')

    print ('\n')
    if dividedBy == "GENDERS" or dividedBy == "ODDS/EVENS":
        numGroups = 2
    else:
        numGroups = int(input('How many groups are there? '))

    time.sleep(2)
    print('\n\n')
    
    for i in range(numGroups):
        groups.append({})

    # dividedBy: genders
    if dividedBy == 'GENDERS':
        for student in students:
            if student['Gender'] == 'boy':
                if len(groups[0]) == 0:
                    groups[0]['name'] = 'Group ' + 'BOYS'
                    groups[0]['roster'] = []
                groups[0]['roster'].append(student)
            elif student['Gender'] == 'girl':
                if len(groups[1]) == 0:
                    groups[1]['name'] = 'Group ' + 'GIRLS'
                    groups[1]['roster'] = []
                groups[1]['roster'].append(student)

    # dividedBy: odds/evens
    if dividedBy == 'ODDS/EVENS':
        for student in students:
            if (int(student['#']) % 2) != 0:
                if len(groups[0]) == 0:
                    groups[0]['name'] = 'Group ' + 'ODDS'
                    groups[0]['roster'] = []
                groups[0]['roster'].append(student)
            else:
                if len(groups[1]) == 0:
                    groups[1]['name'] = 'Group ' + 'EVENS'
                    groups[1]['roster'] = []
                groups[1]['roster'].append(student)

    # dividedBy: sections
    if dividedBy == 'SECTIONS':
        numPerSection = []
        groupInd = 0
        baseNumStud = len(students) // numGroups
        remNumStud = len(students) % numGroups

        for i in range(numGroups):
            numPerSection.append(baseNumStud)
            groups[i]['name'] = 'Group ' + str(i + 1)
            groups[i]['roster'] = []

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
            if len(groups[groupInd]['roster']) < numPerSection[groupInd]:
                groups[groupInd]['roster'].append(student)
                #print(f"{len(groups[groupInd])}. {student['Name']} ({student['#']})")
            else:
                groupInd += 1
                groups[groupInd]['roster'].append(student)
                #print('Moving onto group ' + str(groupInd))
                #print(f"{len(groups[groupInd])}. {student['Name']} ({student['#']})")

        
    # dividedBy: random groups
    if dividedBy == 'RANDOM GROUPS':
        while len(students) >= 1:
            if break_out_flag == True:
                break
            for i, group in enumerate(groups):
                if len(group) == 0:
                    group['name'] = 'Group ' + str(i+1)
                    group['roster'] = []
                randStud = random.choice(students)
                group['roster'].append(randStud)
                #print(f"{randStud['Name']} is going to group {i+1}")
                students.pop(getIndexFromID(students, randStud['id']))
                if len(students) == 0:
                    break_out_flag = True
                    break
    
    
    # dividedBy: every Nth student
    if dividedBy == 'EVERY NTH STUDENT':
        while True:
            i = 0
            for student in students:
                if len(groups[i]) == 0:
                    groups[i]['name'] = 'Group ' + str(i+1)
                    groups[i]['roster'] = []
                groups[i]['roster'].append(student)
                if i < len(groups)-1:
                    i += 1
                else:
                    i = 0
            break

    # Displays students in each group
    display.displayGroups(groups)
        
    while True:
        print('Is there anything that needs to be changed? (Y/N)')
        response = input('>>> ')
        if response.upper().startswith('Y'):
            groups = editGroups(groups)
        elif response.upper().startswith('N'):
            display.displayGroups(groups)
            break
    # Returns a list of dictionaries [{'name': '1', 'roster': [STUDENTS INFO, STUDENTS INFO]}, {'name': '1', 'roster': [STUDENTS INFO, STUDENTS INFO]}]
    #print(groups)
    return groups

def editGroups(groups):
    EDIT_OPTIONS = {'1': 'changeGroupName',
                    '2': 'addStudent',
                    '3': 'removeStudent',
                    '4': 'moveStudent',
                    '5': 'shuffleStudents'}
    
    editedGroups = groups
    #print('This is editGroups()')
    
    while True:
        for key, value in EDIT_OPTIONS.items():
            print("  %s. %s" % (key, value))

        response = input('>>> ')

        if response in EDIT_OPTIONS:
            choice = EDIT_OPTIONS[response]

            if choice == 'changeGroupName':
                editedGroups = changeGroupName(editedGroups)
                break
            elif choice == 'addStudent':
                addStudent()
            elif choice == 'removeStudent':
                removeStudent()
            elif choice == 'moveStudent':
                editedGroups = moveStudent(groups)
            elif choice == 'shuffleStudents':
                editedGroups = shuffleStudents(editedGroups)
            break
        else:
            print('Incorrect input...')

    return editedGroups

def changeGroupName(groups):
    break_out_flag = False
    print('This is changeGroupName')

    while True:
        print('Which group needs its name changed?')
        for i, group in enumerate(groups):
            print(f"  {i+1}. {group['name']}")
        response = input('>>> ')
        
        for group in groups:
            if response.upper() == group['name'].upper():
                # TODO: Fix so groups can't have the same name
                newName = input(f"What should {group['name']}'s new name be? ")
                group['name'] = newName
                break_out_flag = True
                break
        
        if break_out_flag == True:
            break

    return groups

def exists():
    return

def moveStudent(groups):
    break_out_flag = False
    print('Which student do you want to move?')
    print('Enter their name or 4-digit id...')
    targetStudent = input('>>> ')

    for group in groups:
        for student in group['roster']:
            if targetStudent.upper() == student['Name'].upper():
                print(f"The student {targetStudent} is in {group['name']}")
                targetStudent = student
                group['roster'].remove(student)
                break_out_flag = True
                break
        if break_out_flag == True:
            break
    break_out_flag = False

    print(f"Where do you want to move {targetStudent['Name']}?")
    targetGroup = input('>>> ')
    for group in groups:
        if targetGroup == group['name']:
            group['roster'].append(targetStudent)



    return groups

def addStudent():
    return

def removeStudent():
    return

def shuffleStudents(groups):
    for group in groups:
        random.shuffle(group['roster'])
    return groups