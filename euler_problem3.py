#!/usr/bin/python
#Filename: euler_problem3

#variables used(j, i, p, z, k, b, a)
j = 600851475143



#defined functions

def is_prime(j):
    for i in range(2,j):
        if j %  i == 0:
            return False
    return True

def max(p):
    p.sort()
    p[-1]

#my lists
sum = [71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937]
prime = [ ]


#for i in range(2,600851475143):
#    if 600851475143 % i == 0:
#        sum.append(i)
#        print(sum)

for z in sum:
    if is_prime(z) == True:
        prime.append(z)

prime.sort()
b = (len(prime))

greatest_number = prime[b-1]
print(greatest_number)

    

# for each number less than 600851475143
# test if it evenly divides 600851475143
# if it does, is it prime?
    # if it is, set it to the largest prime
# if it doesn't, skip it

    
    


