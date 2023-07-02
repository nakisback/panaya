import time, shutil

WIDTH = shutil.get_terminal_size()[0] - 1
HEIGHT = shutil.get_terminal_size()[1] - 5

def textDisplay():
    print('textDisplay.py')
    return

def getTerminalSize():
    print(shutil.get_terminal_size())

def countdown(num):
    print('Are you ready kids?')
    time.sleep(2)
    print('Aye! Aye! Captain!')
    time.sleep(2)
    print('OHHHHHHHHHHHHHHHH!!!!!!!!!')
    time.sleep(3)

    for i in range(num, -1, -1):
        time.sleep(0.5)
        starMaker(i)
    time.sleep(0.5)
    return

def bookCountdown():

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


    return


def displayGroups(groups):
    #print('This is displayGroups...')
    for group in groups:
        #print(f"Group {group['name']} Roster")
        #print(group['roster'])
        #time.sleep(3)
        header = ' ' + group['name'] + ' (' + str(len(group['roster'])) + ' ppl.) '
        print(header.center(60, '='))
        string = ' '
        for i, student in enumerate(group['roster']):
            studentInfo = student['Name'] + ' (# ' + str(student['#']) + ')'
            if student != group['roster'][-1]:
                studentInfo += ', '
            else:
                studentInfo += '\n'
            if i % 4 == 0 and i != 0:
                string += '\n '
            string += studentInfo

        print(string)

def displayStudentInfo():
    return

def optionsPrompt(string, **options):
    print(string)

    print(options)
    print('asdf')
    for arg in options.values():
        for k, v in arg:
            print(k, v)

    input('>>>')
    return

def displayString(string):
    blockWidth = WIDTH
    blockHeight = HEIGHT
    numCharInBlockWall = 2
    stringBoxWidth = WIDTH - (numCharInBlockWall * 2)
    stringBoxHeight = HEIGHT - (numCharInBlockWall * 2)
    isEven = False
    isEvenSubtract = 1

    if stringBoxHeight % 2 == 0:
        isEven = True
        isEvenSubtract = 0

    for i in range(numCharInBlockWall):
        print('#' * blockWidth)

    for i in range(stringBoxHeight):
        if (stringBoxHeight-isEvenSubtract) / 2 == i:
            print('#' * numCharInBlockWall, end='')
            print(string.center(stringBoxWidth, ' '), end='')
            print('#' * numCharInBlockWall)
        else:
            row = '#' * numCharInBlockWall + ' ' * stringBoxWidth + '#' * numCharInBlockWall
        print(row)

    for i in range(numCharInBlockWall):
        print('#' * blockWidth)

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