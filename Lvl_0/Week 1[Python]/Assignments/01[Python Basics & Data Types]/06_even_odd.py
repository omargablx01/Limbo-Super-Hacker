#!/usr/bin/python3
the_num = int(input("Type Number For Check even 0R odd : "))

def even_odd(num):
    if the_num % 2 == 0 :
        print(f"Your Number : {num} is Even")
    else:
        print(f"Your Number : {num} is Odd")
even_odd(the_num)


#result = "Even" if the_num > 0 and the_num % 2 == 0 else "Odd" if the_num > 0 else "Negative or Zero"
#print(result) # P and Even
