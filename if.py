#!/usr/bin/python
#Filename: if.py

number = "Zach"
guess = str(input('Enter an name : '))

if guess == number:
    print('Congratulations, you guessed it.') #New block starts here
    print('(but you don\'t win any prizes!)') #New block ends here


elif guess != number:
    print('No, it is a not that name')
    #you must have guess > number to reach here

print('Done')
#this last statement is always executed, after the if statement is executed
