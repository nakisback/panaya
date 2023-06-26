#! python3
# countdown.py
"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import os, sys, time
import sevseg # Imports our sevseg.py program.


while True: # Main program loop:
    while True: # User prompt loop
        response = []
        print('How much time should the countdown be? (Enter "mm:ss" or "QUIT")')
        response = input('> ')
        #print('How many seconds should the countdown be?')
        #response = input('> ')
        if response.upper() == 'QUIT':
            print('Quitting the application...')
            time.sleep(3)
            sys.exit()

        colonIndex = response.find(':')
        if colonIndex == -1:
            print('Please format your answer with a ":".')
            time.sleep(2)
            continue

        if not response[:colonIndex].isdecimal() or not response[colonIndex + 1:]:
            print('Please enter a whole number.')
            time.sleep(2)
        else:
            minutesLeft = int(response[:colonIndex])
            secondsLeft = int(response[colonIndex + 1:])
            totalSecondsLeft = minutesLeft * 60 + secondsLeft
            break
        

    try:
        while True: 
            # Clear the screen by printing several newlines:
            #print('\n' * 60)
            os.system('cls')

            # Get the hours/minutes/seconds from secondsLeft:
            # For example: 7265 is 2 hours, 1 minute, 5 seconds.
            # So 7265 // 3600 is 2 hours:
            hours = str(totalSecondsLeft // 3600)
            # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
            minutes = str((totalSecondsLeft % 3600) // 60)
            # And 7265 % 60 is 5 seconds:
            seconds = str(totalSecondsLeft % 60)

            

            # Get the digit strings from the sevseg module:
            hDigits = sevseg.getSevSegStr(hours, 2)
            hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

            mDigits = sevseg.getSevSegStr(minutes, 2)
            mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

            sDigits = sevseg.getSevSegStr(seconds, 2)
            sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

            # Display the digits:
            print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
            print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
            print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

            if totalSecondsLeft == 0:
                print()
                print('    * * * * BOOM * * * *')
                fireworks = '''
                                                         .''.
           .''.      .        *''*    :_\/_:     .
          :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
      .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
     :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_'.':'.'
     : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
      '..'  ':::' === * /\ *     .'/.\'.  ' ._____
          *        |   *..*         :       |.   |' .---"|
            *      |     _           .--'|  ||   | _|    |
            *      |  .-'|       __  |   |  |    ||      |
         .-----.   |  |' |  ||  |  | |   |  |    ||      |
     ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
    jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      &                    ~-~-~-~-~-~-~-~-~-~   /|
     ejm97    )      ~-~-~-~-~-~-~-~  /|~       /_|\\
            _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
    ~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
    ~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
    ''' 
                for row in fireworks.splitlines():
                    print(row)
                    time.sleep(0.3)
                time.sleep(2)
                print('Another countdown? (Y/N)') 
                response = input('> ')
                if response.upper() == 'Y':
                    break
                else:
                    print('Exiting the program...')
                    time.sleep(2)
                    sys.exit()

            print()
            print('Press Ctrl-C to quit.')

            time.sleep(1) # Insert a one-second pause.
            totalSecondsLeft -= 1
    except KeyboardInterrupt:    
        print('Countdown, by Al Sweigart al@inventwithpython.com')
        sys.exit() # When Ctrl-C is pressed, end the program.)

input()


















