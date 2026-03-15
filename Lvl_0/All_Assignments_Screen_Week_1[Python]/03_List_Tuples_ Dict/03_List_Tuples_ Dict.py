
# t~ >>>>                                            Assignments  03_List_Tuples_ Dict                                     <<<<<
# ? --------------------------------- 1,2  ------------------------- 01_02_ten_tools.py
#!/usr/bin/python3
# my_list = ["Nmap","MetaSploit","Wireshark","Burp Suite","JohnTheRipper","sqlmap","msfvenom","hydra","tcpdump","sslsplit"]

# print(f"3rd => {my_list[2]}")
# ? --------------------------------- 3,4  ------------------------- 03_04_count.py
#!/usr/bin/python3
# all_text = "llgl ooo sss nn ff g"
# print(f"String Befor Count ( '{all_text}' )")
# print("-"*40)
# counts = {}
# for char in all_text:
#     counts[char] = counts.get(char, 0) + 1

# for key,value in counts.items():
#     print(f"{key} => {value}")
# ? --------------------------------- 5  ------------------------- 05_sort.py
#!/usr/bin/python3
# my_list = [115,1,458,2,5,89,4,6,7,4,3,748,415,15,9,12,33,489,412,-1]
# lens = len(my_list)
# print(f"Before Sort => {my_list}")
# for i in range(lens):
#     for j in range(0, lens - i - 1):
#         if my_list[j] > my_list[j + 1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print("-"*90)
# print(f"After Sort => {my_list}")

# ? --------------------------------- 6  ------------------------- 06_ports.py
#!/usr/bin/python3
# ports_services = {
#     21: "FTP",
#     22: "SSH",
#     23: "Telnet",
#     25: "SMTP",
#     53: "DNS",
#     80: "HTTP",
#     110: "POP3",
#     123: "NTP",
#     143: "IMAP",
#     161: "SNMP",
#     443: "HTTPS",
#     445: "SMB",
# }
# input_port = int(input("Write Port > "))

# def get_service_name(port_number):
#     service = ports_services.get(port_number, "Service Not Found")
#     return service

# service_name = get_service_name(input_port)
# print(f"Port {input_port} Service Is : {service_name}")
# ? --------------------------------- 7  ------------------------- 07_remdup.py
#!/usr/bin/python3
# my_list = [9,6,7,9,6,7,1,1,2,2,3,3,4,4,-1,-1]
# print(f"Befor Remove Duplicate : {my_list}")
# print("-"*70)
# def remove_duplicates(arr):
#     unique = []
#     for item in arr:
#         if item not in unique:
#             unique.append(item)
#     return sorted(unique)
# print(f"After Remove Duplicate : {remove_duplicates(my_list)}")
# ? --------------------------------- 8  ------------------------- 08_comma.py
#!/usr/bin/python3
# comma_list = ['apple', 'banana', 'cherry']
# print(f"My List > {comma_list}")
# my_comma = ", ".join(comma_list)
# print("-"*40)
# print(f"After Comma > {my_comma}")
# ? --------------------------------- 9  ------------------------- 09_longest.py
#!/usr/bin/python3
# comma_list = ['aaas', 'aaaz', 'aaa']
# print(f"My List > {comma_list}")
# print("-"*40)
# max_len = max(comma_list,key=len)
# print(f"Longest Word > '{max_len}'")
# ? --------------------------------- 10  ------------------------- 10_user_pass.py
#!/usr/bin/python3
# username_passwd = {
#     "admin" : "$TR0NG@@#pa$$w0rd_admin",
#     "root" : "$TR0NG@@#PA$$W0RDDAA_root",
#     "administrator" : "Adm!n!$trat0R"
# }
# input_pass = input("Write UserName > ")
# def user_pass(input_pass):
#     result = username_passwd.get(input_pass,"Username No't In DB")
#     return result

# username = user_pass(input_pass)
# print("-"*40)
# print(f"Username {input_pass} Passwd Is : {username}")
