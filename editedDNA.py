"""DNA animation created by Al Sweigart.
while learning how to program in python, I took this animation idea and 
edited it so that I would understand how the language worked.
In doing so, I found a shortened and easier way to create the animation.
"""

import random, sys, time

pause = 0.15

DNAlist = [
    '          ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}-------{}#',
    '     #{}------{}#',
    '      #{}----{}#',
    '       #{}--{}#',
    '       #{}-{}#',
    '        ##',
    '       #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '      #{}------{}#',
    '       #{}------{}#',
    '        #{}------{}#',
    '         #{}----{}#',
    '          #{}-{}#',
    '           ##']

try:
    time.sleep(1)
    while True:
        randomSelection = random.randint(1,4)
        if randomSelection == 1:
            leftSelection, rightSelection = 'A','T'
        elif randomSelection == 2:
            leftSelection, rightSelection = 'T','A'
        elif randomSelection == 3:
            leftSelection, rightSelection = 'C','G'
        elif randomSelection == 4:
            leftSelection, rightSelection = 'G','C'

        for x in DNAlist:
            print(x.format(leftSelection,rightSelection))
            time.sleep(pause)
        
except KeyboardInterrupt:
    sys.exit()
        