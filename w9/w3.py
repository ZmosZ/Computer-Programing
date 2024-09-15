a = int(input())
x = []

for i in range(a):
    b = int(input())
    x.append(b)
print(sum(x)/a)
x.sort()
print(x[(a-1)//2])