# namePicker.py
# Picks an inputted amount of random names from a classroom excel workbook.
# namePicker.py G2-1.xlsx 6 questions
# namePicker.py G2-1.xlsx 5 questions skipCd
# namePicker.py G2-1.xlsx 3 books - Picks 3 boys and 3 girls to pass books out

#TODO:(Complete) Make sure everyone gets a fair share of turns
#TODO: Reformat the list to call on a different student for a specific question
#TODO: Count how many times each student has been called for each
# category (questions vs. books)


from tempfile import NamedTemporaryFile
import os, sys, openpyxl, random, time, csv
import shutil

FIELDS = ['id', '#', 'Name', 'Gender', 'Count']
HEIGHT = shutil.get_terminal_size()[1]

def main():
    #print('\n' * HEIGHT)
    #print('HEIGHT: ' + str(HEIGHT))
    if len(sys.argv) > 2:
        filename = str(sys.argv[1])

        students = []
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
                #print(row)

    num = sys.argv[2]

    if len(sys.argv) == 4:
        if sys.argv[3] == 'books':
            thing = 'books'
        elif sys.argv[3] == 'brooms':
            thing = 'brooms'
        elif sys.argv[3] == 'volunteers':
            thing = 'as volunteers'

        bookPasser(students, num, thing) # numQ is actually number of students to pass books out

    
    elif sys.argv[2] == 'reset':
        num = 0
        updateCSVfile(students)
    else:
        numQ = int(sys.argv[2])
        questionAllocator(students, num)

        
    #print('getMaxCount: ' + str(getMaxCount(students)))



#input()


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


def bookPasser(students, num, thing):
    print('\n' * HEIGHT)
    boyCount = 0
    girlCount = 0
    count = 0
    num = int(num)

    #print('len(called)**should be 0**: ' + str(len(called)))

    if thing == 'books':
        action = 'pass out books'
    elif thing == 'brooms':
        action = 'sweep the floor'
    elif thing == 'volunteers':
        action = 'do whatever he needs you to do'
        
    
    print('***********************************************************')
    print('***********************************************************')
    print('Eenie, meenie, miney, mo...')
    time.sleep(2)
    print('Catch a tiger by its toe...')
    print('***********************************************************')
    print('***********************************************************')
    time.sleep(2)
    #print('\n' * HEIGHT)
    print('These ' + str(num) + ' students can help Teacher Tony ' + action + '!!!!!')
    if thing == 'books':
        print('Take only 2-3 books at a time.')
    time.sleep(2)


    # TODO

    maxBoy = (num // 2)
    maxGirl = (num // 2)

    if num % 2 != 0:
        RNG = random.randint(0,1)
        if RNG == 0:
            maxBoy += 1
        else:
            maxGirl += 1

    #print(maxBoy, maxGirl)

    called = []
    #print('len(called)**should be 0**: ' + str(len(called)))

    while len(called) < num:
        randStud = random.choice(students)
        if randStud not in called:
            if randStud['Gender'] == 'boy' and boyCount < maxBoy:
                #print(len(called))
                called.append(randStud)
                boyCount += 1
            if randStud['Gender'] == 'girl' and girlCount < maxGirl:
                #print(len(called))
                called.append(randStud)
                girlCount += 1
        
            
            
        #print(str(len(called)) + '. (#' + str(randStud['#']) + ') ' + str(randStud['Name']))

    #print('len(called): ' + str(len(called)))
    for i in range(len(called)):
        print(str(i+1) + '. (#' + str(called[i]['#']) + ') ' + str(called[i]['Name'])) 
        time.sleep(1)


def questionAllocator(students, numQ):
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

    totalCalled = []

    notCalled = getNotCalled(students)
    calledThisRound = []

    # Change later
    numQ = int(sys.argv[2])

    for qNum in range(numQ):
        randStudent = random.choice(notCalled)

        
        print('*****Question ' + str(qNum+1) + '. (#' + str(randStudent['#']) + ') ' + str(randStudent['Name']))
        time.sleep(1)
        
        randStudInd = getIndexFromID(notCalled, randStudent['id'])
        notCalled.pop(randStudInd)
        calledThisRound.append(randStudent)
        totalCalled.append(randStudent)

        if len(calledThisRound) >= len(students):
            #print('Clearing calledThisRound...')
            calledThisRound.clear()

        if len(notCalled) == 0:
            #print('Getting a new notCalled list...')
            notCalled = getNotCalledThisRound(students, calledThisRound)
            #print(notCalled)
            #print('************')
            

    #for i in range(len(notCalled)):
        #print(str(i) + '. ' + str(notCalled[i]['Name']) + ' ' + str(notCalled[i]['id']))


    '''print('len(students): ' + str(len(students)))
    print('len(notCalled): ' + str(len(notCalled)))
    print('len(calledThisRound): ' + str(len(calledThisRound)))'''

    #nicePrint(totalCalled)
    
    updateCSVfile(totalCalled)

def updateCSVfile(totalCalled):
    filename = sys.argv[1]
    #print(filename)

    # Asks user if they want to save new data.

    while True:
        print('\n' * 3)
        print('Save this data? (Y/N)')
        response = input('> ')
        if response.upper().startswith('N') == True:
            #print('response: ' + str(response.upper()))
            print('Not saving new data...')
            break
        elif response.upper().startswith('Y') == True:
            #print('response: ' + str(response.upper()))
            print('Saving new data...')
            
            
            tempfile = NamedTemporaryFile(mode='w', delete=False)
            #fields = ['id', '#', 'Name', 'Gender', 'Count']

            with open(filename, 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=FIELDS)
                writer = csv.DictWriter(tempfile, fieldnames=FIELDS, lineterminator = '\n')
                for row in reader:
                    for student in totalCalled:
                        if row['id'] == student['id']:
                            #print('updating row (%s) %s' % (str(row['id']), str(row['Name'])))
                            count = int(row['Count'])
                            count += 1
                            row['Count'] = count
                            #row['#'], row['Name'], row['Gender'], row['Count'] = student['#'], student['Name'], student['Gender'], student['Count']
                    if sys.argv[2] == 'reset':
                        if row['Count'] != 'Count':
                            #print('resetting count')
                            row['Count'] = 0
                    row = {'id': row['id'], '#': row['#'], 'Name': row['Name'],
                           'Gender': row['Gender'], 'Count': row['Count']}
                    #print(row)
                    writer.writerow(row)
                    

            shutil.move(tempfile.name, filename)
            break

        else:
            print('Something went wrong...')
            

def getMaxCount(students):
    maxCount = 0
    for student in students:
        if maxCount < int(student['Count']):
            maxCount = int(student['Count'])
    return maxCount


def getNotCalled(students):
    maxCount = getMaxCount(students)
    notCalled = []
    for student in students:
        if int(student['Count']) < maxCount:
            notCalled.append(student)

    if len(notCalled) == 0:
        for student in students:
            notCalled.append(student)
    return notCalled

def getNotCalledThisRound(students, calledThisRound):
    notCalled = []
    for student in students:
        notCalled.append(student)
    #print('function getNotCalledThisRound')
    #print(notCalled)

    #print('#####')
    #print('len(calledThisRound): ' + str(len(calledThisRound)))
    #print(calledThisRound)
    for calledStudent in calledThisRound:
        ind = getIndexFromID(notCalled, calledStudent['id'])
        notCalled.pop(ind)

    #print('len(notCalledThisRound): ' + str(len(notCalled)))
    #print('&&&&&')
        
    return notCalled

def getIndexFromID(List, ID):
    for i in range(len(List)):
        if str(ID) == str(List[i]['id']):
            index = i

    return index

def nicePrint(List):
    for i in range(len(List)):
        print(str(i) + '. ', end='')
        print(List[i])


#TODO: 
# Counts # per gender, # that haven't been called yet this round
#def classStats():
    


if __name__ == "__main__":
    main()


