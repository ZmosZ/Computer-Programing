from math import *
x = []
a = int(input())
def Zscore ():
    for i in range(a):
        l = input()
        s = l.split(" ")
        x.append(int(s[2]))
        avg = sum(x)/len(x)
        ss = 0
    for i in x:
        ss = (ss+(i-avg)**2)
        sd = round(sqrt(ss/a),2)
    for i in range(a):
        zs = (x[i]-avg)
        zd = round(zs/sd,2)
        print(zd)
Zscore()