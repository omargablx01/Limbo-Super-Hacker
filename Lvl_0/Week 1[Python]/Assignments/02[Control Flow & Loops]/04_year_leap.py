#!/usr/bin/python3

the_year = int(input("Type Year For Check Leap Year | No : "))
#if the_year % 4 == 0:
    
#    if the_year % 100 == 0:
#        
#        if the_year % 400 == 0:
#           
#            print(f"{the_year} is leap Year") 
#        else:
#            print(f"{the_year} Not Leap Year")  
#    else:
#        print(f"{the_year} is leap Year")
#else:
#    print(f"{the_year} Not Leap Year")
    
#print('-' * 70 )

#print(f"    Two Way To Check  built-in ' isleap ' function    ")

#print('-' * 70 )

import calendar 

# Use the built-in isleap function to check if the year is a leap year
if calendar.isleap(the_year):
    print(f"{the_year} is leap Year") 
else:
    print(f"{the_year} Not Leap Year")
