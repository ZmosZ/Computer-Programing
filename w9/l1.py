x = []
a = int(input())
for i in range (a):
    b = input()
    x.append(b)
c = int(input())
for i in range(c):
    d = int(input())
    if d < a+1 and b >=0:
        print(x[b])
    else:
        print('No Name')