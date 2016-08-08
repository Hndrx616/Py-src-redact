'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
import itertools

c=raw_input("\nPLEASE ENTER CHARACTERS [E.G Abc124&@#] BY WHICH YOU WANT TO MAKE DICTIONARY : ")
x=raw_input("PLEASE ENTER MAXIMUM LENGTH : ")
file2 =open('dictionary.txt','w')
res = itertools.product(c, repeat=int(x)) # 3 is the length of your results
for i in res:
	file2.write("\n"+''.join(i))
file2.close()