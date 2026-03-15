#!/usr/bin/python3
correct_password = "STR0ng@#!Pa$$w00rd_not~easy"
invalid_attempts = 0
while True :
    passwd = input("Write Password : ")
    if passwd == correct_password :
        print("Access granted!")
        break
    else :
        invalid_attempts += 1
        print("-"*30)
        print(f"Incorrect password. {invalid_attempts} Try Again ..")
