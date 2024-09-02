#ข้อ 8
a = int(input())
for i in range(a):
    for j in range(a-i):
        print(str(j+1)+"|",end="")
    print("")