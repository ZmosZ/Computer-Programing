from csv import *
try:
    with open('a1.csv','r')as f:
        r = reader(f)
        l = list(r)
        s = 0
        for i in range (len(l)):
            s = s+int(l[i][0])
        avg = s / len(l)
        print(avg)
except Exception as e:
    print(e)

try:
    with open ('a2.csv','w')as x:
        w =writer(x,lineterminator='\n')
        w.writerow([avg])
except Exception as e:
    print(e)