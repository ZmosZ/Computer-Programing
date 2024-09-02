a = int(input())
x = []

for i in range(a):
    b = int(input())
    x.append(b)
mean = sum(x)/(len(x))
data = sorted(x)
n = (len(data))
if n % 2 ==0:
    median = data[n//2-1]
else:
    median = data[n//2]

print('mean: ',mean)
print('median: ',median)