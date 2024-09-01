# ข้อ 18
a = int(input())

for i in range(1,a+1,1):
    for j in range(a-i):
        print("  ",end="")
    for j in range(i):
        print(str(j+1)+"|",end="")
    for j in range(i-1):
        print(str(i-j-1)+"|",end="")
    print("")