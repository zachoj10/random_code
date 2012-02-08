#!/usr/bin/python
#Filename: func_global.py

x = 50

def add(n):
    global x, h
    x = 15
    
    h = 10
    
    print('h is', h)
    h = x + n
    print('Changed global h to', h)
    return h

def test():
    global x

    print('x is', x)
    x = 23
    print('Changed global x to', x)
    

a = add(5)
print('Value of h is', h)

#test()
print('Value of x is', x)
