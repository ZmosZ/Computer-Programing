from csv import *
try:
    l1 = []
    l2 = []
    a1 =[]
    a2 =[]
    with open('c1.csv','r',encoding='utf-8')as f:
        r = reader(f)
        l1 = list(r)
    with open('c2.csv','r',encoding='utf-8')as f:
        r = reader(f)
        l2 = list(r)
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
    with open('c3.csv','w',encoding='utf-8')as f:
        w = writer (f,lineterminator='\n')
        w.writerows(l1)
    with open('c1.txt', 'r', encoding='utf-8') as f:
        a1 = [line.strip().split() for line in f]
    with open('c2.txt', 'r', encoding='utf-8') as f:
        a2 = [line.strip().split() for line in f]
    for i in a1:
        check = 0
        for j in a2:
            if i[0] == j[0]:
                i.append(j[1])
                check = 1
                break
        if check == 0:
            i.append('-')
    with open('c3.txt', 'w', encoding='utf-8') as f:
        for line in a1:
            f.write(' '.join(line) + '\n')
except Exception as e:
    print(e)