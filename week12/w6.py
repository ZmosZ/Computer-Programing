from csv import *
try:
    with open('a.csv','r',encoding='utf-8')as f:
        r = reader(f)
        l = list(r)
    f = open('a.txt','r',encoding='utf-8')
    a = f.read()
    print(a)
    f.close()
except Exception as e:
    print(e)