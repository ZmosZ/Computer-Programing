a =[]
a.append(0)
a.append(1)
for i in range(100):
    b = a[i] + a[i+1]
    a.append(b)
c = int(input())
print(a[c])