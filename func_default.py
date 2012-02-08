#!/usr/bin/python
#Filename: func_default.py

import Test1

def say(message = 'Hello', n = 1, g = 17):
    print(message * n, g)
    
say()
say('Hola \
Amigo')
say('World' , g = 12)


