#!/usr/bin/python3
tries = 3
admins = ['root','admin','ntfsx00']
while tries > 0:
    login = input("Type User For Login : ")
    if login in admins:
        print(f"Successful Login You Are Admin User ( {login} ) ..")
        break
    else:
        tries -=1
        print(f"Access denied. Try again .. Your Tries is {tries}")
        if tries == 0 :
            print('-'* 45)
            print("Access denied. Your System Is Shutdown .. Byee!")
            print('-'* 45)
