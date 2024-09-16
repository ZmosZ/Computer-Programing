s = []
for i in range(5):
    a = int(input())
    s.append(a)
def allsum(s):
    r = 0
    for i in range(5):
        r += s[i]
    return r
print(allsum(s))