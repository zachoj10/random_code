#!/usr/bin/python
#Filename: objvar.py

class Robot:
    '''Represents a robot, with a name'''
    
    #A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initizlizes the data'''
        self.name = name
        print('(Initizlizing {0})'.format(self.name))

        #When this person is created, the robot
        #adds to the population

        Robot.population += 1
    
    def __del__(self):
        '''I am dying.'''
        print('{0} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was that last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.\
format(Robot.population))

    def sayHi(self):
        '''Greeting by the robot.

        Yeah, they can do that.'''
        print('Greetings, my masters call me {0}.'.format(self.name))

    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here. \n")

print("Robots have finished their work.  So let's destroy them.")
del droid1
del droid2

Robot.howMany()
