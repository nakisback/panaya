# callers.py
# questionAllocator(students, num)
# bookPasser(students, num, choice, text)
# groupQuestions(students, num)

import time, random, os, csv, sys, shutil, keyboard
import display
from tempfile import NamedTemporaryFile
from helpers import getNotCalled, generateNotCalled, getNotCalledThisRound, getIndexFromID

FIELDS = ['id', '#', 'Name', 'Gender', 'qCount', 'bCount']
HEIGHT = shutil.get_terminal_size()[1]

def test():
    print("This is callers.py")

def questionAllocator(path, students, num):
    totalCalled = []
    notCalled = getNotCalled(students, 'qCount')
   
    # calledThisRound[] --> Used so each student is at least called once
    calledThisRound = []
    
    while True:
        response = input('Show results one-by-one using ENTER?(Y/N):  ')
        if response.upper().startswith('Y') == True:
            wait = True
            pretext = ''
            break
        elif response.upper().startswith('N') == True:
            wait = False
            #pretext = '***** Question '
            break
    print('*' * 50)
    pretext = '***** Question '

    # Countdown timer display
    if response.upper().endswith('CD') == True:
        print('Are you ready kids?')
        time.sleep(2)
        print('Aye! Aye! Captain!')
        time.sleep(2)
        print('OHHHHHHHHHHHHHHHH!!!!!!!!!')
        time.sleep(3)
        for number in range(5,-1,-1):
            time.sleep(0.5)
            starMaker(number)
        time.sleep(0.5)

    for qNum in range(num):
        randStudent = random.choice(notCalled)
        if response.upper().endswith('CD') == True:
            time.sleep(1)
        string = pretext + str(qNum+1) + '. (#' + str(randStudent['#']) + ') ' + str(randStudent['Name'])
        # randStudInd --> index of randStudent from notCalled list
        # Removes randStudent from notCalled list based on its index
        randStudInd = getIndexFromID(notCalled, randStudent['id'])
        notCalled.pop(randStudInd)
        
        calledThisRound.append(randStudent)
        totalCalled.append(randStudent)

        # ???
        if wait == True:
            if input(string).upper().startswith('S'):
                break
        else:
            print(string)


        # TODO: make dictionary with key-item pairs being qCount-students
        # ex. -> maxCount = 6
        # {'4': [student1],
        #  '5': [student2, student3, student4,student5],
        #  '6': [student6]}
        if len(calledThisRound) >= len(students):
            #print('Clearing calledThisRound...')
            calledThisRound.clear()

        if len(notCalled) == 0:
            #print('Getting a new notCalled list...')
            notCalled = getNotCalledThisRound(students, calledThisRound)
            #print(notCalled)
            #print('************')

##    print('len(students): ' + str(len(students)))
##    print('len(notCalled): ' + str(len(notCalled)))
##    print(notCalled)
##    print('len(calledThisRound): ' + str(len(calledThisRound)))

    if response.upper().endswith('CD') == True:
        input('Press ENTER to continue...')

    print('\n' * 3)
    
    updateCSVfile(path, totalCalled, 'qCount')

def questionAllocatorTemp(path, students, num):
    notCalled = generateNotCalled(students, 'qCount')
    totalCalled = []
    display.starMaker(10)

    for k, v in notCalled.items():
        print(f"Group {k}:")
        random.shuffle(v)
        for student in v:
            print(f"  {student['Name']} (#{student['#']}): {student['qCount']}")
    
    while True:
        response = input('Show results one-by-one using ENTER?(Y/N):  ')
        if response.upper().startswith('Y') == True:
            wait = True
            pretext = ''
            break
        elif response.upper().startswith('N') == True:
            wait = False
            #pretext = '***** Question '
            break
    print('*' * 50)
    pretext = '***** Question '

    # Countdown timer display
    if response.upper().endswith('CD') == True:
        print('Are you ready kids?')
        time.sleep(2)
        print('Aye! Aye! Captain!')
        time.sleep(2)
        print('OHHHHHHHHHHHHHHHH!!!!!!!!!')
        time.sleep(3)
        for number in range(5,-1,-1):
            time.sleep(0.5)
            starMaker(number)
        time.sleep(0.5)


    #print(notCalled)
    qNum = 0
    while qNum < num:
        for k, vList in notCalled.items():
            for student in vList:
                if qNum == num:
                    break
                else:
                    print(f"{student['Name']} (#{student['#']}): {student['qCount']}")
                    totalCalled.append(student)
                    qNum += 1

        
    for qNum in range(num):
        print('###')
        print(notCalled)
        print('###')
        randStudent = random.choice(notCalled)
        if response.upper().endswith('CD') == True:
            time.sleep(1)
        string = pretext + str(qNum+1) + '. (#' + str(randStudent['#']) + ') ' + str(randStudent['Name'])
        ##string = f"{pretext}{qNum+1}. (#{})"
        

        # ???
        if wait == True:
            if input(string).upper().startswith('S'):
                break
        else:
            print(string)


        # TODO: make dictionary with key-item pairs being qCount-students
        # ex. -> maxCount = 6
        # {'4': [student1],
        #  '5': [student2, student3, student4,student5],
        #  '6': [student6]}

        if len(notCalled) == 0:
            #print('Getting a new notCalled list...')
            notCalled = getNotCalledThisRound(students, calledThisRound)
            #print(notCalled)
            #print('************')

    if response.upper().endswith('CD') == True:
        input('Press ENTER to continue...')

    print('\n' * 3)
    
    updateCSVfile(path, totalCalled, 'qCount')

def bookPasser(path, students, num, choice, text):
    #os.system('cls')
    num = int(num)
    boyCount = 0
    girlCount = 0
    maxBoy = (num // 2 + random.randint(0,1))
    maxGirl = num - maxBoy
    called = []
    notCalled = getNotCalled(students, 'bCount')
    random.shuffle(notCalled)

    print('\n' * int(HEIGHT/2))
    print('***********************************************************')
    print('***********************************************************')
    print('Eenie, meenie, miney, mo...')
    time.sleep(2)
    print('Catch a tiger by its toe...')
    print('***********************************************************')
    print('***********************************************************')
    time.sleep(2)
    #print('\n' * HEIGHT)
    print('These ' + str(num) + ' students can help Teacher Tony by ' + text + '!!!!!')
    if choice == 'BOOKS':
        print('Take only 2-3 books at a time.')
    time.sleep(2)

    while len(called) < num:
        if len(notCalled) == 0:
            notCalled = getNotCalledThisRound(students, called)
        else:
            randStud = random.choice(notCalled)
##            print('called: ', end='')
##            print(called)
##            print('notCalled: ', end='')
##            print(notCalled)
##            print("randStud " + str(randStud["Name"]))
            if randStud not in called:
                if randStud['Gender'] == 'boy' and boyCount <= maxBoy:
                    #print(len(called))
                    called.append(randStud)
                    notCalled.pop(getIndexFromID(notCalled, randStud['id']))
                    boyCount += 1
                if randStud['Gender'] == 'girl' and girlCount <= maxGirl:
                    #print(len(called))
                    called.append(randStud)
                    notCalled.pop(getIndexFromID(notCalled, randStud['id']))
                    girlCount += 1
##                print('len(called): ' + str(len(called)))
##                print('num: ' + str(num))
##                print('*************')
            
            
            #print(str(len(called)) + '. (#' + str(randStud['#']) + ') ' + str(randStud['Name']))

    #print('len(called): ' + str(len(called)))
    for i in range(len(called)):
        print(str(i+1) + '. (#' + str(called[i]['#']) + ') ' + str(called[i]['Name'])) 
        time.sleep(1)

    input('Press ENTER to continue...')

    updateCSVfile(path, called, 'bCount')

# Each group gets called once per round
def groupQuestions(path, students, num):
    #MAX_BOY = 0
    #MAX_GIRL = 0
    qNum = 0
    boys = []
    girls = []
    called = []
    GROUPS = [boys, girls]
    break_out_flag = False

    #numGroups = int(input('Number of Groups: '))
    # dividedBy: gender, odds/evens, sectioned, random
    #grps = groupsMaker(students, numGroups, dividedBy='gender')
    grps = groupsMaker(students)

    for i, grp in enumerate(grps):
        print(f"Group {i+1}: \n{grp}")

    random.shuffle(grps)


    print('After shuffling...')
    for grp in grps:
        print(f"\nGroup {grp['name']}: \n{grp}")

    # TODO(5/6/23): Move students from a large group to a smaller group to make things even

##    for student in students:
##        if student['Gender'] == 'boy':
##            boys.append(student)
##        else:
##            girls.append(student)
##
##    # TODO: Shuffle the GROUPS list to determine the order
##    groupOrder = []
##    print('  # of boys:  ' + str(len(boys)))
##    print('  # of girls: ' + str(len(girls)))
##    print()
##    if len(boys) == len(girls):
##        #print('There are the same amount of boys as girls in this class!')
##        print('  Rolling the dice to see goes first...')
##        for i in range(3):
##            print('  .')
##        if random.randint(0,1) == 1:
##            print('  BOYS GO FIRST!!!')
##            groupOrder.append(boys)
##            groupOrder.append(girls)
##        else:
##            print('  GIRLS GO FIRST!!!')
##            groupOrder.append(girls)
##            groupOrder.append(boys)
##    elif len(boys) < len(girls):
##        # More girls --> Girls go first so students get a chance to answer at least 1 question
##        print('  GIRLS GO FIRST!!!')
##        groupOrder.append(girls)
##        groupOrder.append(boys)
##    elif len(boys) > len(girls):
##        # More boys --> Same thing as above
##        print('  BOYS GO FIRST!!!')
##        groupOrder.append(boys)
##        groupOrder.append(girls)
##
##    random.shuffle(boys)
##    random.shuffle(girls)

    time.sleep(2)

    round = 0
    input('\n\n  Press ENTER to begin...')
    while qNum < num:
        print('\n  Round ' + str(round+1))
        time.sleep(1)

        for group in groupOrder:
            if qNum < num:  # TODO: repetitive... try changing
                ind = round % len(group)
                if group[ind]['Gender'] == 'boy':
                    pretext = '  b'
                elif group[ind]['Gender'] == 'girl':
                    pretext = '  g'
                response = input(f"  {pretext}{ind+1}. (#{group[ind]['#']}) {group[ind]['Name']}")
                called.append(group[ind])
                if response.upper().startswith('S') == True:
                    break_out_flag = True
                    break
                time.sleep(1)
                qNum += 1
        if break_out_flag == True:
            break
          
        round += 1

    updateCSVfile(path, called, 'qCount')
    

    print()


def groupsMaker(students):
    break_out_flag = False
    
    # dividedBy: gender, odds/evens, sectioned, random
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
                    groups[0]['name'] = 'BOYS'
                    groups[0]['roster'] = []
                groups[0]['roster'].append(student)
            elif student['Gender'] == 'girl':
                if len(groups[1]) == 0:
                    groups[1]['name'] = 'GIRLS'
                    groups[1]['roster'] = []
                groups[1]['roster'].append(student)

    # dividedBy: odds/evens
    if dividedBy == 'ODDS/EVENS':
        for student in students:
            if (int(student['#']) % 2) != 0:
                if len(groups[0]) == 0:
                    groups[0]['name'] = 'ODDS'
                    groups[0]['roster'] = []
                groups[0]['roster'].append(student)
            else:
                if len(groups[1]) == 0:
                    groups[1]['name'] = 'EVENS'
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
            groups[i]['name'] = str(i + 1)
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
                    group['name'] = str(i+1)
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
                    groups[i]['name'] = str(i+1)
                    groups[i]['roster'] = []
                groups[i]['roster'].append(student)
                if i < len(groups)-1:
                    i += 1
                else:
                    i = 0
            break

    # Displays students in each group
    #print(groups)
    for i, group in enumerate(groups):
        #print(f"Group {group['name']} Roster")
        #print(group['roster'])
        count = 0
        #time.sleep(3)
        print(f"Group {group['name']} ({len(group['roster'])} ppl.): ")
        for student in group['roster']:
            if count < 4:
                count += 1
                print(f"{student['Name']} (#{student['#']})", end='')
            else:
                count = 1
                print(f"\n{student['Name']} (#{student['#']})", end='')
            if student != group['roster'][-1]:
                print(', ', end='')
        print('\n')
        
    return groups

def updateCSVfile(path, totalCalled, cType, **kwargs):
    print('\n' * 3)
    for i in range(3):
        time.sleep(0.5)
        print('.\n\n')
    time.sleep(1)
        
    print('These students need to be updated:')
    for i, called in enumerate(totalCalled):
        print(str(i+1) + '. (#' + str(called['#'])+') ' + called['Name'])

    # Asks user if they want to save new data.

    while True:
        print()
        prompt = 'Save this data? (Y/N)'
        print(prompt)
        response = input('> ')
        if response.upper().startswith('N') == True:
            print('Not saving new data...')
            time.sleep(2)
            break
        elif response.upper().startswith('Y') == True:
            
            print('\nSaving new data...')
            for i in range(3):
                time.sleep(1)
                print('.')
            time.sleep(1)
            
            tempfile = NamedTemporaryFile(mode='w', delete=False)

            with open(path, 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=FIELDS)
                writer = csv.DictWriter(tempfile, fieldnames=FIELDS, lineterminator = '\n')
                for row in reader:
                    for student in totalCalled:
                        if student['id'] == '' or student['id'] == None:
                            raise Exception('updateCSVfile -- Student does not have a valid id...')
                        if row['id'] == student['id']:
                            #print('updating row (%s) %s' % (str(row['id']), str(row['Name'])))
                            count = int(row[cType])
                            count += 1
                            row[cType] = count
                            #row['#'], row['Name'], row['Gender'], row['Count'] = student['#'], student['Name'], student['Gender'], student['Count']
##                    if response.upper().startswith('R') == True:
##                        if row[cType] != cType:
##                            #print('resetting count')
##                            row[cType] = 0
                    row = {'id': row['id'], '#': row['#'], 'Name': row['Name'],
                           'Gender': row['Gender'], 'qCount': row['qCount'],
                           'bCount': row['bCount']}
                    #print(row)
                    writer.writerow(row)
        
            try:
                shutil.move(tempfile.name, path)

                print('SAVE COMPLETED SUCCESSFULLY')
                break
            except PermissionError:
                print("Uh oh.... The .csv file is probably still open...")
                time.sleep(1)
                print("Please close the file and try again.")
                time.sleep(2)
                print("\n" * 3)
                

        else:
            for i in range(5):
                time.sleep(0.5)
                print('.')
            time.sleep(1)
            print("Incorrect input...")



def starMaker(cdNum):
    star = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5JJ5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GJ7!JP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ?. ?JB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&YJ:  :JJ#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5J~    ^JY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@PJ!      !JP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ?        ?JB@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&&&&&&&&###BYJ.        .JYB###&&&&&&&@@@@@@@@@@@@@@@@@
@@@@@@@#PYYYYJJJJJJJ?????7777^          ^777?????JJJJJYYYYYY5P#@@@@@@@
@@@@@@@@@#PJJ!^.....                             ......^!?JP#@@@@@@@@@
@@@@@@@@@@@&B5J!^                 """ + str(cdNum) + """!                 :!J5G&@@@@@@@@@@@
@@@@@@@@@@@@@@#PY?~.                              .~?YP#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&B5J7^                          ^!J5B&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#PY?~.                    .~?YP#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&GYJ:                  ^JYB&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@BJ7                    ?J#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@YJ:                    ^JY@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@GJ7          ::          7JB@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&YJ:       :~7JJ7~:       :JY&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@PJ!     :~7JPB&&B5J7~:     7JG@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#J?.  :!?YPB&@@@@@@&BPJ7~:  .JY&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@PJ!:!?YPB&@@@@@@@@@@@@&BPY?~:!JP@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#JJ?YP#&@@@@@@@@@@@@@@@@@@&BPY?JJ&@@@@@@@@@@@@@@@@@@
"""
    for line in star.splitlines():
        print(line)
        time.sleep(0.01)
    if cdNum == 0:
        
        for i in range(2):
            print('**********************************************************************')




def spongebobMaker():
    spongebob = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@GJ?JY55J7?JY55J??JYPGGGP55PBBGPPPB#BGG#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@&J^^:....:^^:..........:....:::....:::^:~G@@@@@@@@@@@@@@@@@@@
@@@@@@@&G?^^^~.:.^7777^~~.:5!.!7.:.:?^.~Y..^::!7~:Y@@@@@@@@@@@@@@@@@@@
@@@@@@B!:~??~~^:.:~~~^.~G!~?!^YJ^.:^Y?^!J^7P^.::.^G@@@@@@@@@@@@@@@@@@@
@@@@&P7:^JJJ!:~^:.:~:.~~.       ~7~:      .^~:...^B@@@@@@@@@@@@@&&@@@@
@@@&J::^^7J?^^^~::::.~!     ^7?7.^~ ^!7!:   :!.:::Y@@@@@@@@@@@B?7G@@@@
@@@@5~:^^^^^:^^!::::.7:    :JB@&J.~:Y#@GY.   7::.:5@@@@@@@@@@P~5&@@@@@
@@@@@B7:^^^~~^:~^.::.^!.... ~?Y?^7^ !Y5J~  .^7::.!#@@@@@@@PJG??P@@@@@@
@@@@@@5^:^7JJ^:^~:::.^^:::^^:.:^~^~^..:::^^::~?..~#@@@@@@5:~?J^^Y@@@@@
@@@@@@&J^^?J7^^^~.:::::^?!.:~^^:...^!~~^^^~!77^..^G@@@@@@B!^^~~Y&@@@@@
@@@@@@@@P^^^^7J?~::::::.JB?~^::::::.^~!?J7~^:..::?&@@@@@@@B^YP#@@@@@@@
@@@@@@@@&~::^JJJ~~:::::.JBBBGPP!~~YPJ^^?7!:.:::::P@@@@@@@&~5@@@@@@@@@@
@@@@@@@@@P!::!?!:~:.:::.?BGGGGB!~~P#Y::7^..^777^.5@@@@@@&~Y@@@@@@@@@@@
@@@@@@@@@@#!::^^^~^.:::.7#GGBGGBBBGBP:::::.^!!~::5BG&@@B~Y@@@@@@@@@@@@
@@@@@@@@@@@G!~~J7^~::~:.:YJ7?YYJYPB#7.::::::~^.:7::?J5J7G@@@@@@@@@@@@@
@@@@@@@@@@@? :7!^:~::^~~::!!7?????PY:.:::::!!~::~ .?5#&@@@@@@@@@@@@@@@
@@@@@@@@@@B   ^~^^^::!7~:.:::^^^^::::::..:::::.^PBB#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@B~::~7^^^!^^^^^!!^^^^~!~~!!^^~!^:::^!P@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@Y?Y7!~^?..  .:^~^^^:~GG7:~~~^.... J@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@5!B###PGJYPPPPY?5PPPGPPGGPG5JPGGG5G@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@G~BPPPPGJY5555YJ5555PPPG555YJ5555YB@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@P.7##BGG5YYYYYYYYYYYY55YYYYY555555#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#:..?@@B555555P&@@@@@@@GP555P#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@P~:YYB@@&BJGB#&@@@@@@@@@G7&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@&GJY@@@@@#:#@@@@@@@@@@@@5!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#~&@@@@@@@@@@@@5?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#~&@@@@@@@@@@@@Y?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@B:#@@@@@@@@@@@@PY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&B@@@@@@@@@@&@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""


    for line in spongebob.splitlines():
        print(line)
        time.sleep(0.01)











