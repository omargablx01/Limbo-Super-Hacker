#!/usr/bin/python3

import random

tries = 4

print(f"You Have {tries} attempts To Try Guessing Game ..! ")

first = int(input("First Num : "))

last = int(input("last Num : "))

print(f"First Numer Is : {first} last Number is {last}")
if first < last :
    while tries > 0 :
        
        rand_num = int(input("Type Your Guessing Number : "))

        ran = random.randint(first,last)

        if rand_num == ran :

            print(f"Congratulations! You guessed number Is {rand_num} in {tries-1} attempts")

            break

        else :
            tries -=1

            print(f"Sorry Worng Number Try Again *_* .. Your Tries Is : {tries}")

            if tries == 0 :
                print("-"*30)
                print(f"Sorry Worng Number You'r over your attempts Is : {tries}")
                print("-"*30)
                
else :
    print(f"{first} First Number Is Under 0r Equal {last}")
