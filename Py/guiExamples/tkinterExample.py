from Tkinter import *

def msg():
	print('hello stdout...')

top = Frame()
top.pack()
Label(top, text='Hello world').pack(side=TOP)
widget = Button(top, text='pres', command=msg)
widget.pack(side=BOTTOM)
top.mainloop()