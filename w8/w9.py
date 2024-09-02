#ข้อ 9
a = int(input())
for i in range(a):
    for j in range(a-i-1):
        print("  ",end="")
    for j in range(i + 1):
        print(str(j+1)+"|",end="")
    print("")
