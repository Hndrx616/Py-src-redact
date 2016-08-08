'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
from java.util import Date
start = Date()

numbers = ['0','1','2','3','4','5','6','7','8','9']
uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = ["'",'|','\\','?','.','+','-','&&','||','!','(',')','{','}','[',']','^','~','*','?',':','"']

# all possible ascii characters
chars	= numbers + uppers + lowers + specials
# base conversion
base	= len(chars)
# number of attempts
n		= 0

# variables
password	= event.source.parent.getComponent('Password Field').text
solution	= event.source.parent.getComponent('solution')
solved		= False

solution.text = ''

if password == '':
	solution.text = 'Your password is empty'
	solved = True
elif password == chars[n]:
	solution.text = 'Your password is ' + chars[n]
	solved = True
else:
	n += 1

# convert base 10 integer n into base b
def numberToBase(n, b):
	digits = []
	while n:
		digits.append(int(n % b))
		n /= b
	return digits[::-1]

# test passwords
if solved == False:
	while n < 99999999:
		lst = numberToBase(n,base)
		word = ''
		for x in lst:
			word += chars[x]

		solution.text = word

		# solved passwrod
		if password == word:
			solution.text = word
			solved = True

			end = Date()
			time = str((end.time-start.time)/1000.0) + ' s'
			print '____Statistics____'
			print 'Password ' + word
			print 'Attempts ' + str(n)
			print 'Time: ' + time
			break

		# not solved
		else:
			n += 1

if solved == False:
	solution.text = 'unsolved after %d attempts' % n