# ข้อ 16
x = int(input())
y = True
for i in range (2,x):
    if(x%i ==0):
        print("No prime number")
        y = False
        break
if y:
    print("prime number")