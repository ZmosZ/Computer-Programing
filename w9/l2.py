x = []
y = []
while True:
    s = input()
    if s == 'STOP':
        break
    t = s.split()
    name = t[0]
    score = int(t[1])
    x.append(name)
    y.append(score)
m = x.index(max(score))
mn = x.index(min(score))
print(m,mn)
