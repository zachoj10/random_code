#!/usr/bin/python
#Filename: func_nonlocal.py


def func_outer():
    global x
    x = 2
    print('x is', x)

    def func_inner():
        global x
        
        x = 5

    func_inner()
    print('Changed local x to', x)

func_outer()

print('The value of x is', x)
