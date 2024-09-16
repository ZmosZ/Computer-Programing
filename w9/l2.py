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
if y:
    max_index = y.index(max(y))
    min_index = y.index(min(y))
    print(x[max_index])
    print(x[min_index])
