import os

target = input("Input target: ")

os.system(f"nmap -A -p 80 {target} -v >> nmap.txt")
os.system(f"smbclient -N -L {target}")