from tkinter import *
from csv import *
f = Tk()
f.minsize(400,600)
f.maxsize(400,600)
n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()
n5 = StringVar()
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
r = StringVar()
Label(f,text='Name').place(x=50,y=25)
Label(f,text='Score').place(x=200,y=25)
Entry(f,textvariable=n1).place(x= 50,y=50)
Entry(f,textvariable=s1).place(x= 200,y=50)
Entry(f,textvariable=n2).place(x= 50,y=100)
Entry(f,textvariable=s2).place(x= 200,y=100)
Entry(f,textvariable=n3).place(x= 50,y=150)
Entry(f,textvariable=s3).place(x= 200,y=150)
Entry(f,textvariable=n4).place(x= 50,y=200)
Entry(f,textvariable=s4).place(x= 200,y=200)
Label(f,textvariable=r).place(x=150,y=300)
def GPA():
    try:
        L = []
        L.append(int(s1.get()))
        L.append(int(s2.get()))
        L.append(int(s3.get()))
        L.append(int(s4.get()))
        r.set('GPA :'+str(sum(L)/ len(L) ))
    except Exception as e:
        print(e)
def SAVE():
    try:
        a = [ [ n1.get(), s1.get() ] ,
             [n2.get(),s2.get()] ,
             [n3.get(),s3.get()],
             [n4.get(),s4.get()]]
        with open ('b.csv','w',encoding='utf-8')as f:
            w = writer(f, lineterminator='\n')
            w.writerows(a)
    except Exception as e:
        print(e)
        
def LOAD():
    try:
        with open('b.csv','r',encoding='utf-8')as f:
            r = reader(f)
            l = list(r)
            n1.set (l[0] [0]); s1.set(l[0] [1])
            n2.set (l[1] [0]); s2.set(l[1] [1])
            n3.set (l[2] [0]); s3.set(l[2] [1])
            n4.set (l[3] [0]); s4.set(l[3] [1])
    except Exception as e:
        print(e)
Button(f,text='GPA',command=GPA).place(x=150,y=350)
Button(f,text='SAVE',command=SAVE).place(x=150,y=400)
Button(f,text='LOAD',command=LOAD).place(x=150,y=450)