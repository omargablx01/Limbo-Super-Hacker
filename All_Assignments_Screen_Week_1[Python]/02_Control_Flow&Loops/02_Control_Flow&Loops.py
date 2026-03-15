
# t~ >>>>                                            Assignments  02_Control_Flow&Loops                                     <<<<<
# ? --------------------------------- 1  ------------------------- 01_ask_passwd.py
#!/usr/bin/python3
# passwd = input("Type Your Pw : ")
# allows = ["s3cr3t"]
# if passwd in allows:
#     print("Allows Access ..!")
# else:
#     print("NoT Have Allow Access :( .. ")
# ? --------------------------------- 2  ------------------------- 02_divisible4.py
#!/usr/bin/python3
# for ex in range(1,101):
#     if ex % 4 != 0:
#         print(f"Not Divisible 4 > {ex}")
# ? --------------------------------- 3  ------------------------- 03_4digit_PIN.py
#!/usr/bin/python3
# for pin in range(0000,9999):
#     if pin > 999:
#         print(f"You 4-digit PIN Code : {str(pin).zfill(4)}")
# ? --------------------------------- 4  ------------------------- 04_year_leap.py
#!/usr/bin/python3
# the_year = int(input("Type Year For Check Leap Year | No : "))
# if the_year % 4 == 0:
    
#    if the_year % 100 == 0:
       
#        if the_year % 400 == 0:
          
#            print(f"{the_year} is leap Year") 
#        else:
#            print(f"{the_year} Not Leap Year")  
#    else:
#        print(f"{the_year} is leap Year")
# else:
#    print(f"{the_year} Not Leap Year")
    
#print('-' * 70 )

#print(f"    Two Way To Check  built-in ' isleap ' function    ")

#print('-' * 70 )
#! ---------------- OR
# import calendar 

# Use the built-in isleap function to check if the year is a leap year
# if calendar.isleap(the_year):
#     print(f"{the_year} is leap Year") 
# else:
#     print(f"{the_year} Not Leap Year")

# ? --------------------------------- 5  ------------------------- 05_prime_num.py
#!/usr/bin/python3
# for num in range(1,101):
#     if num > 1 :
#         for i in range(2,num):
#             if (num % i ) == 0 :
#                 # print(f"{num} Is N0T Prime Number")
#                 break
#         else:
#             print(f"{num} Is Prime Number")
            
# ''' Other Biult-in Function '''

#from sympy import isprime

#for i in range(1,101):
#    prime = isprime(i)
#    if prime == True:
#        print(f"{i} Is Prime Number")
#    else:
#        print(f"{i} Is N0T Prime Number")
# ? --------------------------------- 6  ------------------------- 06_login3.py
#!/usr/bin/python3
# tries = 3
# admins = ['root','admin','ntfsx00']
# while tries > 0:
#     login = input("Type User For Login : ")
#     if login in admins:
#         print(f"Successful Login You Are Admin User ( {login} ) ..")
#         break
#     else:
#         tries -=1
#         print(f"Access denied. Try again .. Your Tries is {tries}")
#         if tries == 0 :
#             print('-'* 45)
#             print("Access denied. Your System Is Shutdown .. Byee!")
#             print('-'* 45)
# ? --------------------------------- 7  ------------------------- 07_guessing_game.py
#!/usr/bin/python3
# import random
# tries = 4
# print(f"You Have {tries} attempts To Try Guessing Game ..! ")
# first = int(input("First Num : "))
# last = int(input("last Num : "))
# print(f"First Numer Is : {first} last Number is {last}")
# if first < last :
#     while tries > 0 :
#         rand_num = int(input("Type Your Guessing Number : "))
#         ran = random.randint(first,last)
#         if rand_num == ran :
#             print(f"Congratulations! You guessed number Is {rand_num} in {tries-1} attempts")
#             break
#         else :
#             tries -=1
#             print(f"Sorry Worng Number Try Again *_* .. Your Tries Is : {tries}")
#             if tries == 0 :
#                 print("-"*30)
#                 print(f"Sorry Worng Number You'r over your attempts Is : {tries}")
#                 print("-"*30)
                
# else :
#     print(f"{first} First Number Is Under 0r Equal {last}")

# ? --------------------------------- 8  ------------------------- 08_fizz_buzz.py
#!/usr/bin/python3
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} > FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} > Fizz")
#     elif i % 5 == 0:
#         print(f"{i} > Buzz")
#     else:
#         print(i)
# ? --------------------------------- 9  ------------------------- 09_while_passwd.py
#!/usr/bin/python3
# correct_password = "STR0ng@#!Pa$$w00rd_not~easy"
# invalid_attempts = 0
# while True :
#     passwd = input("Write Password : ")
#     if passwd == correct_password :
#         print("Access granted!")
#         break
#     else :
#         invalid_attempts += 1
#         print("-"*30)
#         print(f"Incorrect password. {invalid_attempts} Try Again ..")

# ? --------------------------------- 10  ------------------------- 10_palindrome.py
#!/usr/bin/python3

# my_string = input("Write Palindrome String : ")

# if my_string == my_string[::-1]:
#     print(f"( {my_string[::-1]} ) Is Palindrome")
# else:
#     print(f"( {my_string} ) No't palindrome")

#@@ With Reversed Function OR

#rev = ''.join(reversed(my_string))

#if my_string == rev:
#    print("palindrome")
#else:
#    print("No't palindrome")
