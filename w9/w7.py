x = []
y = []
i = 0
while(True):
    s = input()
    t = s.split()
    name = t[0]
    score = int(t[1])
    if name == "-1" or score == -1:
        break
    x.append(name)
    y.append(score)
    i = i + 1
print(sum(y)/i)