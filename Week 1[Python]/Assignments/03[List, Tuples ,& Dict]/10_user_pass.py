#!/usr/bin/python3
username_passwd = {
    "admin" : "$TR0NG@@#pa$$w0rd_admin",
    "root" : "$TR0NG@@#PA$$W0RDDAA_root",
    "administrator" : "Adm!n!$trat0R"
}
input_pass = input("Write UserName > ")
def user_pass(input_pass):
    result = username_passwd.get(input_pass,"Username No't In DB")
    return result

username = user_pass(input_pass)
print("-"*40)
print(f"Username {input_pass} Passwd Is : {username}")
