#!/usr/bin/python
#Filename: using_list.py

#This is my shopping list

fives = [ ]
threes = [ ]

sum = 0

for i in range(0,1000):
    if i % 5 == 0:
        sum += i
    elif i % 3 == 0:
        sum += i
    

print(sum)
