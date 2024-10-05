from csv import *
try:
    with open('a.csv','r',encoding='utf-8')as f:
        r = reader(f)
        l = list(r)
    print(l)
    f.close()
except Exception as e:
    print(e)