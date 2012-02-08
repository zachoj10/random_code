#!/usr/bin/python
#Filename: continue.py

number = 23
running = True
while running:
    s = int(input('Enter an integer : '))
    if s == number:
        print('Congratulations, {0} is the correct number' .format(s))
        running = False
    elif s < number:
        print('Sorry, {0} is too low'. format(s))
        
    else:
        print('Sorry, {0} is too high.' .format(s))
        
    

    
