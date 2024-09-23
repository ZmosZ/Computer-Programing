from tkinter import *
f = Tk()

def x1():
    t = int(s2.get()) - int(s3.get())
    s1.set(t)
def x2():
    t = int(s2.get()) + int(s3.get())
    s1.set(t)
def x3():
    t = int (s2.get()) * int(s3.get())
    s1.set(t)
s2 = StringVar()
Entry(f,textvariable=s2).pack()
s3 = StringVar()
Entry(f,textvariable=s3).pack()
s1 = StringVar()
Label(f,textvariable=s1).pack()
Button(f,text='-',command=x1).pack()
Button(f,text='+',command=x2).pack()
Button(f,text='X',command=x3).pack()