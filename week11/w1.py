from tkinter import *
f = Tk()
f.minsize(400,400)
f.maxsize(400,400)

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()

r = StringVar()

l1 = Label(f,text="คะแนนคนที่ 1")
l1.place(x=50,y=50)
e1 = Entry(f,textvariable=s1)
e1.place(x = 150,y =50)

l2 = Label(f,text="คะแนนคนที่ 2")
l2.place(x=50,y=100)
e2 = Entry(f,textvariable=s2)
e2.place(x = 150,y =100)

l3 = Label(f,text="คะแนนคนที่ 3")
l3.place(x=50,y=150)
e3 = Entry(f,textvariable=s3)
e3.place(x = 150,y =150)

l4 = Label(f,text="คะแนนคนที่ 4")
l4.place(x=50,y=200)
e4 = Entry(f,textvariable=s4)
e4.place(x = 150,y =200)

l5 = Label(f,text="คะแนนคนที่ 5")
l5.place(x=50,y=250)
e5 = Entry(f,textvariable=s5)
e5.place(x = 150,y =250)

result = Label(f,textvariable=r)
result.place(x=150,y=300)
r.set("SHOW")

def cal():
    L = []
    L.append(int(s1.get()))
    L.append(int(s2.get()))
    L.append(int(s3.get()))
    L.append(int(s4.get()))
    L.append(int(s5.get()))
    r.set(str('ค่าเฉลี่ย/คะแนนมากสุด/คะแนนน้อยสุด'))
    r.set(str(sum(L) / len(L))+'/'+str(max(L))+'/'+str(min(L)))

d = Button(f,text='CALCULATOR',command=cal)
d.place(x=150,y=350)