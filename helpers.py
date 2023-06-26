# helpers.py
# getMaxCount(students)
# getNotCalled(students)
# getNotCalledThisRound(students, calledThisRound)
# getIndexFromID(List, ID)


# Returns the max amount of times a student has been called for a category
# TODO: filter by category
# TODO: should be called by classname
def getMaxCount(students, cType):
    maxCount = 0

    for student in students:
        if maxCount < int(student[cType]):
            maxCount = int(student[cType])

    #print(f"maxCount: {maxCount}") 
    return maxCount

def getMinCount(students, cType):
    minCount = None

    for student in students:
        #print(f"{student['Name']} {cType}: {student[cType]}")
        if minCount == None:
            minCount = int(student[cType])
        elif int(student[cType]) < minCount:
            minCount = int(student[cType])

    return minCount

def generateNotCalled(students, cType):
    print('generateNotCalled')
    notCalled = {}
    minCount = getMinCount(students, cType)
    maxCount = getMaxCount(students, cType)

    for count in range(minCount, maxCount+1):
        notCalled[count] = []

    for student in students:
        countKey = int(student[cType])
        notCalled[countKey].append(student)

    for k, vList in notCalled.items():
        print(f"len({k}): {len(vList)}")

    print('Did generateNotCalled do the thing with asdf?')
    return notCalled


# A list of students is passed to this function
# Returns a list of students who have not reached the class's maxCount yet
# TODO: Two lists should be passed and maybe a classname
#       (1st: A ref list, 2nd: A list of those already called)
def getNotCalled(students, cType):
    maxCount = getMaxCount(students, cType)
    minCount = getMinCount(students, cType)
    notCalled = []

    for student in students:
        if int(student[cType]) == minCount:
            notCalled.append(student)


    # If everyone has the same maxCount, notCalled gets populated with all
    # students effectively starting a 'new round' for the class. 
    if len(notCalled) == 0:
        for student in students:
            notCalled.append(student)
    '''print('getNotCalled function\nnotCalled: ')
    print(notCalled)
    print('len(notCalled): ' + str(len(notCalled)))'''
    return notCalled

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
        if str(ID) == str(List[i]['id']):
            index = i
    return index
