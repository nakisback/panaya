# callers.py
# questionAllocator(students, num)
# bookPasser(students, num, choice, text)
# groupQuestions(students, num)

import time, random, os, csv, sys, shutil, keyboard, groups
import display
from tempfile import NamedTemporaryFile
from helpers import getCallQueue, getNotCalledThisRound, getIndexFromID

FIELDS = ['id', '#', 'Name', 'Gender', 'qCount', 'bCount', 'jCount']
HEIGHT = shutil.get_terminal_size()[1]
TIME_STANDARD = 1

def questionAllocator(path, students, num):
    notCalled = getCallQueue(students, 'qCount')
    totalCalled = []
    wait = False
    break_out_flag = False

    #display.displayList(students)

    #print('List of Students to be Potentially Called')
    for k, v in notCalled.items():
        #print(f"Group {k} ({len(v)} students):")
        random.shuffle(v)
        #for student in v:
            #print(f"  {student['Name']} (#{student['#']}): {student['qCount']}")
    
    while True:
        response = input('Show results one-by-one using ENTER?(Y/N):  ')
        if response.upper().startswith('Y') == True:
            wait = True
            pretext = ''
            break
        elif response.upper().startswith('N') == True:
            #pretext = '***** Question '
            break
    print('*' * 50)
    pretext = '***** Question '

    # Countdown timer display
    if response.upper().endswith('CD') == True:
        display.countdown(5)

    #print(notCalled)
    qNum = 0
    while qNum < num:
        if break_out_flag == True:
            break
        for k, vList in notCalled.items():
            if break_out_flag == True:
                break
            for student in vList:
                if qNum == num:
                    break
                else:
                    #string = pretext + str(qNum+1) + '. (#' + str(student['#']) + ') ' + str(student['Name'])
                    string = pretext + str(qNum+1) + '. (#' + str(student.studNum) + ') ' + str(student.name)
                    if wait == True:
                        waitResponse = input(string)
                        if waitResponse.upper().startswith('S'):
                            totalCalled.append(student)
                            break_out_flag = True
                            break
                        elif waitResponse.upper().startswith('A'):
                            print('   ###  ABSENT  ###')
                            print('PICKING NEW STUDENT. . .')
                            time.sleep(2 * TIME_STANDARD)
                            continue
                        time.sleep(0.5 * TIME_STANDARD)
                    else:
                        print(string)
                    #print(f"{student['Name']} (#{student['#']}): {student['qCount']}")
                    totalCalled.append(student)
                    #display.displayCalledStudents(totalCalled)
                    qNum += 1
    #display.displayCalledStudents(totalCalled, question="Question ")

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
    totalCalled = []
    script = []
    notCalled = getCallQueue(students, 'bCount')

    display.bookCountdown()
    #script.append('These ' + str(num) + ' students can help Teacher Tony by ' + text + '!!!!!')
    print('These ' + str(num) + ' students can help Teacher Tony by ' + text + '!!!!!')
    if choice == 'BOOKS':
        print('Take only 2-3 books at a time.')
        #script.append('Take only 2-3 books at a time.')
    time.sleep(2 * TIME_STANDARD)

    for k, vList in notCalled.items():
        random.shuffle(vList)

    for k, vList in notCalled.items():
        for student in vList:
            #if student['Gender'] == 'boy':
            if student.gender == 'boy':
                if boyCount < maxBoy:
                    totalCalled.append(student)
                    boyCount += 1
            #elif student['Gender'] == 'girl':
            elif student.gender == 'girl':
                if girlCount < maxGirl:
                    totalCalled.append(student)
                    girlCount += 1

    for i, student in enumerate(totalCalled):
        print(f"{i+1}. (#{student.studNum}) {student.name}")
        time.sleep(1 * TIME_STANDARD)

    input('Press ENTER to continue...')

    updateCSVfile(path, totalCalled, 'bCount')

# Each group gets called once per round
def groupQuestions(path, students, num):
    qNum = 0
    totalCalled = []
    break_out_flag = False

    #print('howd these students go through?')
    #print(students)

    grps = groups.groupsMaker(students)

    # Shuffles grp order
    random.shuffle(grps)

    print("  Group Order:")
    for i, grp in enumerate(grps):
        print(f"    {i+1}. {grp.name}")

    time.sleep(2 * TIME_STANDARD)

    round = 0
    input('\n\n  Press ENTER to begin...')

    print("  Shuffling students around . . . ")
    time.sleep(2 * TIME_STANDARD)
    for grp in grps:
        for count in grp.callQueue.keys():
            random.shuffle(grp.callQueue[count])
            for student in grp.callQueue[count]:
                grp.studentOrder.append(student)

    # grp.callQueue is a dictionary with key-value pair {jCount: [studentList], jCount+1: [studentList]}
    # grp.callQueue.values() is a list of those studentLists  -->  [[studentList1], [studentList2], [studentList3]]
    for grp in grps:
        print(grp.studentOrder)

    while qNum < num:
        print('\n  Round ' + str(round+1))
        time.sleep(1 * TIME_STANDARD)
        
        for grp in grps:
            ind = round % len(grp.studentOrder)
            teamName = str(grp.name)
            response = input(f"  Q{qNum+1}. {teamName} - {grp.studentOrder[ind].name} (#{grp.studentOrder[ind].studNum})")
            totalCalled.append(grp.studentOrder[ind])
            qNum += 1

            if response.upper().startswith('S') == True or qNum == num:
                break_out_flag = True
                break
        if break_out_flag == True:
            break
          
        round += 1

    updateCSVfile(path, totalCalled, 'jCount')
    
    print()

def updateCSVfile(path, totalCalled, cType, **kwargs):
    print('\n' * 3)
    for i in range(3):
        time.sleep(0.5 * TIME_STANDARD)
        print('.\n')
    time.sleep(1 * TIME_STANDARD)
        
    print('These students need to be updated:')
    for i, called in enumerate(totalCalled):
        print(str(i+1) + '. (#' + str(called.studNum)+') ' + called.name)

    # Asks user if they want to save new data.

    while True:
        print()
        prompt = 'Save this data? (Y/N)'
        print(prompt)
        response = input('> ')
        if response.upper().startswith('N') == True:
            print('Not saving new data...')
            time.sleep(2 * TIME_STANDARD)
            break
        elif response.upper().startswith('Y') == True:
            
            print('\nSaving new data...')
            for i in range(3):
                time.sleep(1 * TIME_STANDARD)
                print('.')
            time.sleep(1 * TIME_STANDARD)
            
            tempfile = NamedTemporaryFile(mode='w', delete=False)

            with open(path, 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=FIELDS)
                writer = csv.DictWriter(tempfile, fieldnames=FIELDS, lineterminator = '\n')
                for row in reader:
                    for student in totalCalled:
                        if student.id == '' or student.id == None:
                            raise Exception('updateCSVfile -- Student does not have a valid id...')
                        if row['id'] == student.id:
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
                           'bCount': row['bCount'], 'jCount': row['jCount']}
                    #print(row)
                    writer.writerow(row)
        
            try:
                shutil.move(tempfile.name, path)

                print('SAVE COMPLETED SUCCESSFULLY')
                break
            except PermissionError:
                print("Uh oh.... The .csv file is probably still open...")
                time.sleep(1 * TIME_STANDARD)
                print("Please close the file and try again.")
                time.sleep(2 * TIME_STANDARD)
                print("\n" * 3)
                

        else:
            for i in range(5):
                time.sleep(0.5 * TIME_STANDARD)
                print('.')
            time.sleep(1 * TIME_STANDARD)
            print("Incorrect input...")