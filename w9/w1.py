a = int(input())
x = []

for i in range(a):
    b = int(input())
    x.append(b)
i = max(x)
o = min(x)
avg = (sum(x))/(len(x))
print(i)
print(o)
print(avg)