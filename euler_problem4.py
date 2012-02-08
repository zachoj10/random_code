#!/usr/bin/python
#Filename: euler_problem4


#Variables used(z, k, f, c, l, i)

palindromes = [ ]
sum = [ ]




def ispalindrome(x):
    j=str(x)
    if j==j[::-1]:
        return True
    else:
        return False
    

for z in range(100,1000):
    for i in range(900,1000):
        k = i*z
        f=str(k)
        if f==f[::-1]:
            c=int(f)
            palindromes.append(c)
            print(palindromes)


palindromes.sort()
l = len(palindromes)
print('The largest palindrome formed from the product of two three digit numbers is...')
print(palindromes[l-1])

            
            

#Test for whether something is a palindrome
        



