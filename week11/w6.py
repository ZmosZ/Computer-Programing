from tkinter import *
f = Tk()

def x1():
    if int(s2.get()) >=80:
        s1.set('A')
    elif int (s2.get()) >=70:
        s1.set('B')
    elif int (s2.get()) >=60:
        s1.set('C')
    elif int (s2.get()) >=50:
        s1.set('D')
    elif int (s2.get()) >=0:
        s1.set('F')
    else:
        s1.set("E")
        
s2 = StringVar()
Entry(f,textvariable=s2,).pack()
s1 = StringVar()
l2 = Label(f,textvariable=s1).pack()
Button(f,text="Grade",command =x1).pack()