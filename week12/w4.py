from csv import *
h = []
try:
    with open ('x.csv','r')as y:
        r = reader(y)
        h = list(r)
except Exception as e:
    print(e)

s = 0
for i in range(len(h)):
    s = s+int(h[i][1])
print(s)                                                                                                                        