# callers.py
# questionAllocator(students, num)
# bookPasser(students, num, choice, text)
# groupQuestions(students, num)

import time, random, os, csv, sys, shutil, keyboard, groups
import display
from tempfile import NamedTemporaryFile
from helpers import getNotCalled, generateNotCalled, getNotCalledThisRound, getIndexFromID

FIELDS = ['id', '#', 'Name', 'Gender', 'qCount', 'bCount']
HEIGHT = shutil.get_terminal_size()[1]

def questionAllocator(path, students, num):
    notCalled = generateNotCalled(students, 'qCount')
    totalCalled = []
    break_out_flag = False

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
            wait = False
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
                    string = pretext + str(qNum+1) + '. (#' + str(student['#']) + ') ' + str(student['Name'])
                    if wait == True:
                        if input(string).upper().startswith('S'):
                            totalCalled.append(student)
                            break_out_flag = True
                            break
                        time.sleep(0.5)
                    else:
                        print(string)
                    #print(f"{student['Name']} (#{student['#']}): {student['qCount']}")
                    totalCalled.append(student)
                    qNum += 1

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
    notCalled = generateNotCalled(students, 'bCount')

    display.bookCountdown()
    print('These ' + str(num) + ' students can help Teacher Tony by ' + text + '!!!!!')
    if choice == 'BOOKS':
        print('Take only 2-3 books at a time.')
    time.sleep(2)

    for k, vList in notCalled.items():
        random.shuffle(vList)

    for k, vList in notCalled.items():
        for student in vList:
            if student['Gender'] == 'boy':
                if boyCount < maxBoy:
                    totalCalled.append(student)
                    boyCount += 1
            elif student['Gender'] == 'girl':
                if girlCount < maxGirl:
                    totalCalled.append(student)
                    girlCount += 1

    for i, student in enumerate(totalCalled):
        print(f"{i+1}. (#{student['#']}) {student['Name']} {student['Gender']}")
        time.sleep(1)

    input('Press ENTER to continue...')

    updateCSVfile(path, totalCalled, 'bCount')

# Each group gets called once per round
def groupQuestions(path, students, num):
    #MAX_BOY = 0
    #MAX_GIRL = 0
    qNum = 0
    totalCalled = []
    break_out_flag = False

    #numGroups = int(input('Number of Groups: '))
    # dividedBy: gender, odds/evens, sectioned, random
    #grps = groupsMaker(students, numGroups, dividedBy='gender')
    grps = groups.groupsMaker(students)

    #for i, grp in enumerate(grps):
    #    print(f"Group {i+1}: \n{grp}")

    random.shuffle(grps)


    #print('After shuffling...')
    #for grp in grps:
    #    print(f"\nGroup {grp['name']}: \n{grp}")

    time.sleep(2)

    round = 0
    input('\n\n  Press ENTER to begin...')
    #print(grps)
    #print(len(grps))
    while qNum < num:
        print('\n  Round ' + str(round+1))
        time.sleep(1)
        
        for grp in grps:
            #print('New Group')
            #print(grp)
            ind = round % len(grp['roster'])
            teamName = str(grp['name'])
            #print("grp['roster'][0]['Name']")
            #print(grp['roster'][0]['Name'])
            response = input(f"  Q{qNum+1}. {teamName} - {grp['roster'][ind]['Name']} (#{grp['roster'][ind]['#']})")
            totalCalled.append(grp['roster'][ind])
            qNum += 1

            if response.upper().startswith('S') == True or qNum == num:
                break_out_flag = True
                break
        if break_out_flag == True:
            break
          
        round += 1

    updateCSVfile(path, totalCalled, 'qCount')
    
    print()

def updateCSVfile(path, totalCalled, cType, **kwargs):
    print('\n' * 3)
    for i in range(3):
        time.sleep(0.5)
        print('.\n')
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