#!/usr/bin/python
#Filename: func_param.py

def printMax(a,b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


x = int(input('Enter an integer : '))
y = 7

printMax(x,7)


