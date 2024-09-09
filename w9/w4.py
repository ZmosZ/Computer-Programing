a = int(input())
x = []

for i in range(a):
    b = input()
    x.append(b)
f = input()
if f in x:
    print('Meet')
else:
    print('Miss')