#ข้อ 7
a = int(input())
for i in range(a):
    for j in range(i+1):
        print(str(j+1)+'|',end="")
    print("")