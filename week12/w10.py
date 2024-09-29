from csv import *
l1 = []
l2 = []
with open('c1.csv','r',encoding='utf-8')as f:
    r = reader(f)
    l1 = list(r)
l3 = []
for i in l1:
    check = 0
    for j in l2:
        if(i[0] == j[0]):
            i.append(j[1])
            check = 1
            break
    if check ==0:
        i.append('-')
    with open('b.csv','w',encoding='utf-8')as f:
        w = writer (f,lineterminator='\n')
        w.writerows(l1)