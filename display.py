import time, shutil, csv, os

WIDTH = shutil.get_terminal_size()[0] - 1
HEIGHT = shutil.get_terminal_size()[1] - 5
NUM_CHAR_IN_WALL = 2
PADDING_PER_SIDE = 3
TIME_STANDARD = 1

stringBoxWidth = WIDTH - (NUM_CHAR_IN_WALL * 2)
# This is wrong. This is the stringBoxHeight and the blank space height combined
stringBoxHeight = HEIGHT - (NUM_CHAR_IN_WALL * 2)

def textDisplay():
    print('textDisplay.py')
    return

def getTerminalSize():
    print(shutil.get_terminal_size())

#TODO: (2/8/23) Should return a list of rows so that each row can be displayed one at a time
def displayCalledStudents(called, **pretext):
    print('This is displayCalledStudents')
    CHARACTER = "*"
    print(called)
    wall = CHARACTER * NUM_CHAR_IN_WALL
    ceiling, floor = '', ''


    for i in range(NUM_CHAR_IN_WALL):
        ceiling += "\n" + CHARACTER * WIDTH
        floor += CHARACTER * WIDTH + "\n"
        #print('*' * WIDTH)

    print(ceiling)


    for j, student in enumerate(called):
        content = f"{pretext['question']}{j+1}. {student}"
        print(wall, end='')
        print(' ' * PADDING_PER_SIDE, end='')
        #print(f"{j+1}. {student.name}", end='')
        print(content, end='')
        print(wall.rjust(WIDTH- len(wall)*2 -len(content) - 1, ' '))

    print(floor)
    #displayBorderBox(called)

    return

def displayBorderBox(list):
    #os.system('cls')
    stringLine = "We have {:<5} chickens."
    blankLines = HEIGHT - (NUM_CHAR_IN_WALL * 2) - len(list) - 2
    pretext = '   Question '
    for i in range(NUM_CHAR_IN_WALL):
        print('*' * WIDTH)

    print('*' * NUM_CHAR_IN_WALL, end='')
    print(' ' * int(WIDTH - (NUM_CHAR_IN_WALL * 2)), end='')
    print('*' * NUM_CHAR_IN_WALL)

    for i in range(len(list)):
        #print(list[i])
        string = pretext + str(i+1) + '. (#' + list[i]['#'] + ') ' + list[i]['Name']
        print('*' * NUM_CHAR_IN_WALL, end='')
        print(string, end='')
        print(' ' * (WIDTH - len(string) - 2 * NUM_CHAR_IN_WALL), end='')
        print('*' * NUM_CHAR_IN_WALL)

    for i in range(blankLines):
        print('*' * NUM_CHAR_IN_WALL, end='')
        print(' ' * int(WIDTH - (NUM_CHAR_IN_WALL * 2)), end='')
        print('*' * NUM_CHAR_IN_WALL)

    for i in range(NUM_CHAR_IN_WALL):
        print('*' * WIDTH)
    return

def displayGroups(groups):
    #print('displayGroups')
    #print(groups)
    blockWidth = WIDTH
    blockHeight = HEIGHT
    blankBoxWidth = blockWidth - (NUM_CHAR_IN_WALL * 2)
    #blankBoxHeight = len(list) + (PADDING_PER_SIDE * 2)

    #print('This is displayGroups...')
    for group in groups:
        #print(f"Group {group['name']} Roster")
        #print(group['roster'])
        #time.sleep(3)
        #header = ' ' + group['name'] + ' (' + str(len(group['roster'])) + ' ppl.) '
        header = ' ' + group.name + ' (' + str(len(group.roster)) + ' ppl.) '
        print(header.center(blockWidth, '='))
        stringRow = ' ' * PADDING_PER_SIDE
        #for i, student in enumerate(group['roster']):
        for i, student in enumerate(group.roster):
            studentInfo = student.name + ' (# ' + str(student.studNum) + ')'
            #if student != group['roster'][-1]:
            if student != group.roster[-1]:
                studentInfo += ', '
            else:
                studentInfo += '\n'
            if i % 4 == 0 and i != 0:
                stringRow += '\n' + ' ' * PADDING_PER_SIDE
            stringRow += studentInfo

        print(stringRow)

def displayStudentInfo():
    return

# Takes options dictionary and returns a keyword based on the user's input
def optionsPrompt(options, **prompts):
    valid_response = False

    for k,v in prompts.items():
        print(v)

    while valid_response == False:
        print("Please type in a number option below:")
        for k, v in options.items():
            option_string = '  '
            if type(k) is tuple:
                option_string += k[0] + '. ' + k[1] + ' for '
            else:
                option_string += k + '. '
            
            option_string += v
            print(option_string)

        response = input('>>> ')
        for k, v in options.items():
            if type(k) is tuple:
                if response == k[0] or response.upper() == k[1]:
                    response = k
                    valid_response = True
                    break
            elif response == k:
                #print('It worked....')
                response = k
                valid_response = True
                break
            
        if valid_response == True:
            #print('breaking out')
            break

        if valid_response == False:
            print(f"ERROR: {response} is not a valid response...")
            time.sleep(2 * TIME_STANDARD)
            print('\n\n')
    #print('Returning response: ' + str(response))
    print('')
    

    return response

def displaySentence(string, **kwargs):
    blockWidth = WIDTH
    blockHeight = HEIGHT
    isEven = False
    isEvenSubtract = 1

    if stringBoxHeight % 2 == 0:
        isEven = True
        isEvenSubtract = 0

    for i in range(NUM_CHAR_IN_WALL):
        print('#' * blockWidth)

    for i in range(int(stringBoxHeight)):
        if (stringBoxHeight-isEvenSubtract) / 2 == i:
            for j in range(len(string)):

                print('#' * NUM_CHAR_IN_WALL, end='')
                print(string[j].center(stringBoxWidth, ' '), end='')
                print('#' * NUM_CHAR_IN_WALL)
        else:
            row = '#' * NUM_CHAR_IN_WALL + ' ' * stringBoxWidth + '#' * NUM_CHAR_IN_WALL
        print(row)

    for i in range(NUM_CHAR_IN_WALL):
        print('#' * blockWidth)


def displayList(list):
    blockWidth = WIDTH
    blockHeight = HEIGHT
    blankBoxWidth = blockWidth - (NUM_CHAR_IN_WALL * 2)
    blankBoxHeight = len(list) + (PADDING_PER_SIDE * 2)

    for i in range(NUM_CHAR_IN_WALL):
        print('&' * blockWidth)
    
    for i in range(PADDING_PER_SIDE):
        print('&' * NUM_CHAR_IN_WALL, end='')
        print(' ' * blankBoxWidth, end='')
        print('&' * NUM_CHAR_IN_WALL)

    
    for item in list:
        print('&' * NUM_CHAR_IN_WALL, end='')
        print(' ' * PADDING_PER_SIDE, end='')
        print(item)
    
    
    for i in range(PADDING_PER_SIDE):
        print('&' * NUM_CHAR_IN_WALL, end='')
        print(' ' * blankBoxWidth, end='')
        print('&' * NUM_CHAR_IN_WALL)

    for i in range(NUM_CHAR_IN_WALL):
        print('&' * blockWidth)





def countdown(num):
    print('Are you ready kids?')
    time.sleep(2 * TIME_STANDARD)
    print('Aye! Aye! Captain!')
    time.sleep(2 * TIME_STANDARD)
    print('OHHHHHHHHHHHHHHHH!!!!!!!!!')
    time.sleep(3 * TIME_STANDARD)

    for i in range(num, -1, -1):
        time.sleep(0.5 * TIME_STANDARD)
        starMaker(i)
    time.sleep(0.5 * TIME_STANDARD)
    return

def bookCountdown():
    script = ["Eenie, meenie, miney, mo..."]

    print('\n' * int(HEIGHT/2))
    #print('*' * WIDTH)
    #print('*' * WIDTH)
    #string[j].center(stringBoxWidth, ' '), end=''

    displaySentence(script)
    time.sleep(2 * TIME_STANDARD)
    script.append("Catch a tiger by its toe...")
    displaySentence(script)
    time.sleep(2 * TIME_STANDARD)
    print('*' * WIDTH)
    print('*' * WIDTH)
    time.sleep(2 * TIME_STANDARD)
    #print('\n' * HEIGHT)


    return


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
        time.sleep(0.01 * TIME_STANDARD)
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
        time.sleep(0.01 * TIME_STANDARD)


if __name__ == "__main__":
    FIELDS = ['article', 'animal', 'color', 'size', 'verb']

    print('Did display.py go through???')
    dir = 'C:\\Users\\Nick\\panaya\\wordbank'

    '''with open(path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)'''