# helpers.py
# getMaxCount(students)
# getNotCalled(students)
# getNotCalledThisRound(students, calledThisRound)
# getIndexFromID(List, ID)

import random


# Returns the max amount of times a student has been called for a category
# TODO: filter by category
# TODO: should be called by classname
def getMaxCount(students, cType):
    maxCount = 0

    for student in students:
        if int(maxCount) < int(getattr(student, cType)):
            maxCount = getattr(student, cType)

    #print(f"maxCount: {maxCount}") 
    return int(maxCount)

def getMinCount(students, cType):
    minCount = None
    #print(cType)
    #print(students)

    for student in students:
        '''print(student)
        print(student.bCount)
        print(getattr(student, cType))'''
        if minCount == None:
            #print(student.name * 10)
            minCount = getattr(student, cType)

        elif getattr(student, cType) < minCount:
            minCount = getattr(student, cType)

    return int(minCount)

# Returns a dictionary where the keys are counts and the values are shuffled lists of students who have those specific counts
def getCallQueue(students, cType):
    #print('generateNotCalled')
    callQueue = {}
    minCount = getMinCount(students, cType)
    maxCount = getMaxCount(students, cType)

    for count in range(minCount, maxCount+1):
        callQueue[count] = []

    for student in students:
        #countKey = int(student[cType])
        countKey = int(getattr(student, cType))
        callQueue[countKey].append(student)

    for k, vList in callQueue.items():
        #print(f"len({k}): {len(vList)}")
        random.shuffle(vList)
        #print(vList)

    #print('Did allQueue do the thing with asdf?')
    #print('printing callQueue')
    #print(callQueue)
    return callQueue


# Each student should be picked only once per 'round'
# Returns a list of students who haven't been called 'this round'
def getNotCalledThisRound(students, calledThisRound):
    notCalled = []
    # Populates the notCalled list with all students
    print('APPENDING ALL STUDENTS BACK')
    for student in students:
        notCalled.append(student)

    # Removes the students who've been already called this round from notCalled
    print('REMOVING CALLED STUDENTS FROM notCalled')
    for calledStudent in calledThisRound:
        ind = getIndexFromID(notCalled, calledStudent['id'])
        print(f"Removing {calledStudent['Name']} (#{calledStudent['#']})")
        notCalled.pop(ind)

    for student in notCalled:
        print(f"(#{student['#']}) {student['Name']}")
        
    return notCalled

def getIndexFromID(List, ID):
    if ID == '' or ID == None:
        raise Exception('getIndexFromID: Student does not have a valid id...')
    for i in range(len(List)):
        if str(ID) == str(List[i].id):
            index = i
    return index
