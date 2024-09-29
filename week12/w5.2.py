from csv  import *
try:
    a= input()
    with open('b.csv','w',encoding='utf-8') as f:
        w = writer(f,lineterminator='\n')
        w.writerow([a])
except Exception as e:
    print(e)