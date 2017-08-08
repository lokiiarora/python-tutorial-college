from Tkinter import *

win= Tk()

b1= Button(win,text="one")
b2= Button(win, text="two")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
win.geometry("480x480")
win.title("Phonebook")