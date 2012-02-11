#!/usr/bin/python
#Filename: euler_problem13.py

numbs = [ ] 

with open('euler_problem13_numbs', 'r') as fnumbs:
    for l in fnumbs.readlines():
        numbs.append(int(l))
    
j = sum(numbs)
print(j)        
     
p = str(j)
print(p[0:10])
