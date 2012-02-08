#!/usr/bin/python
#Filename: euler_problem5.py

p = 20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2
twenties = [ ]
nineteens = [ ]
eighteens = [ ]
seventeens = [ ]
sixteens = [ ]
fifteens = [ ]
fourteens = [ ]
thirteens = [ ]
twelves = [ ]
elevens = [ ] 
tens = [ ]
nines = [ ]
eights = [ ]
sevens = [ ]
sixes = [ ]
fives = [ ]
fours = [ ]
threes = [ ]
twos = [ ]

for i in range(1,p):
    if i % 20 == 0:
        twenties.append(i)

for item in twenties:
    if item % 19 == 0:
        nineteens.append(item)

for item in nineteens:
    if item % 18 == 0:
        eighteens.append(item)

for item in eighteens:
    if item % 17 == 0:
        seventeens.append(item)

for item in seventeens:
    if item % 16 == 0:
        sixteens.append(item)

for item in sixteens:
    if item % 15 == 0:
        fifteens.append(item)

for item in fifteens:
    if item % 14 == 0:
        fourteens.append(item)

for item in fourteens:
    if item % 13 == 0:
        thirteens.append(item)

for item in thirteens:
    if item % 12 == 0:
        twelves.append(item)

for item in twelves:
    if item % 11 == 0:
        elevens.append(item)

for item in elevens:
    if item % 10 == 0:
        tens.append(item)

for item in tens:
    if item % 9 == 0:
        nines.append(item)
       
for item in nines:
    if item % 8 == 0:
        eights.append(item)

for item in eights:
    if item % 7 == 0:
        sevens.append(item)

for item in sevens:
    if item % 6 == 0:
        sixes.append(item)

for item in sixes:
    if item % 5 == 0:
        fives.append(item)

for item in fives:
    if item % 4 == 0:
        fours.append(item)

for item in fours:
    if item % 3 == 0:
        threes.append(item)

for item in threes:
    if item % 2 == 0:
        twos.append(item)

twos.sort()
print(twos[0])
        
