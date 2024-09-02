a = int(input())
x = []

for i in range(a):
    b = int(input())
    x.append(b)
mean = sum(x)/(len(x))
data = sorted(x)
n = (len(data))
median_index = n // 2 - 1 if n % 2 == 0 else n // 2
median = data[median_index]

print('mean: ',mean)
print('median: ',median)