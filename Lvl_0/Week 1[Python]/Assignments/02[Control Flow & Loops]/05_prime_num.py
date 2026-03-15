#!/usr/bin/python3
for num in range(1,101):
    if num > 1 :
        for i in range(2,num):
            if (num % i ) == 0 :
                break
        else:
            print(num)
            
''' Other Biult-in Function '''

#from sympy import isprime

#for i in range(1,101):
#    prime = isprime(i)
#    if prime == True:
#        print(f"{i} Is Prime Number")
#    else:
#        print(f"{i} Is N0T Prime Number")
        

