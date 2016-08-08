#!/usr/bin/env python
#HelloWorld.py
import sys
sys.path.append('\\Program Files\\Python\\Lib\\python23.zip\\lib-tk')
import Tkinter
root = Tkinter.Tk()
l = Tkinter.Label(root, text="Hello, world!\nTkinter on PocketPC!\nSee http://pythonce.sf.net.")
b = Tkinter.Button(root, text='Quit', command=root.destroy)
l.pack()
b.pack()
root.mainloop()