import random
from Tkinter import Tk, Label, Button, Entry, StringVar, END, W, E
import tkMessageBox



class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Catalyst Engine")
        
        self.guess = None

        self.message = "Beta Engine"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.guess_button = Button(master, text="Search", command=self.guess_number)
        self.close_button = Button(master, text="Close", command=self.callback)
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.close_button.grid(row=2, column=1)

    def validate(self, new_text):
        if new_text: # the field is being cleared
            self.guess = None
            return True

    def guess_number(self):

        if self.guess is None:
            self.message = 'Enter a Term'
            
        else:
            self.message = ''

        self.label_text.set(self.message)

    def close(self):
        self.entry.delete(END)
    
    def callback(self):
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()