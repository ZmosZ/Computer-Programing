#ข้อ 10
a = int(input())
for i in range(a):
    for j in range(i):
        print(" ",end=" ")
    for j in range(a-i):
        print(str(j+1)+"|",end="")
    print("")