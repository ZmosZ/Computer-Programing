s = []
for i in range(5):
    a = float(input())
    s.append(a)
def allvalue(s):
    r = 0
    for i in range(5):
        r+=s[i]*(i+1)
    return r
print(allvalue(s))