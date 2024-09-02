a = int(input())
x = []

for i in range(a):
    b = int(input())
    x.append(b)

print(sorted(x))
print(sorted(x,reverse=True))