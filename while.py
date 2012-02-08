#!/usr/bin/python
#Filename: while.py

number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, {0} is the correct number' .format(number))
        running = False #this causes the while loop to stop
    elif guess < number:
        print('Sorry, {0} is a little too low' .format(guess))
    else:
        print("No, it\'s a little lower than that.")

else:
    print('The whole loop is over')

print('Done')
              
