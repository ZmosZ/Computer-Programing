from tkinter import *
f = Tk()

s1 = StringVar()

l2 = Label(f, textvariable=s1)
l2.pack()

s1.set("5")

def x1():
    t = int(s1.get()) + 1
    s1.set( t )

def x2():
    t = int(s1.get()) - 1
    s1.set( t )

Button(f,text="+",command=x1).pack()

Button(f,text='-',command=x2).pack()