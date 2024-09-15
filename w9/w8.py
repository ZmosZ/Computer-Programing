a = []
x = int(input())
for i in range(x):
    s = input()
    m = s.split()
    score = int(m[2])
    a.append(score)
print(sum(a)/len(a))