a = int(input())
x = []
n = []

for i in range(a):
    m = input('Name: ')
    p = int(input())
    n.append(m)
    x.append(p)
avg =sum(x)/(len(x))
print(avg)