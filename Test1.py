#!/usr/bin/python
#Filename: Test1

from random import randint

def guess():
    Name = input('Please enter your name : ')
    Number = randint(1,100)
    Running = True


    print('Guess the integer')
    while Running:
        s = int(input('Please enter an integer : '))
        if s == Number:
            print('Great job {0}!  {1} is the correct number.' .format(Name, s))
            Running = False

        elif s > Number:
            print('Sorry {0}, but {1} is higher than the number. Please guess again.' .format(Name, s))

        else:
            print('Sorry {0}, but {1} is lower than the number.  Please guess again.' .format(Name, s))

    print('Done')

