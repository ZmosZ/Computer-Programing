# ข้อ 20
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range (100000,0,-1):
    if (a % i == 0) and (b % i == 0) and (c % i ==0) and(d % i == 0):
        print(i)
        break
# my_min = a
# if a <= b and a<=c and a <= d:
#     my_min = a
# elif b <= a and b<=c and b <= d:
#     my_min = a
# elif c <= a and c<=b and c <= d:
#     my_min = a
# elif d <= a and d<=b and d <= c:
#     my_min = a

# for i in range (my_min,0,-1):
#     if(a % i == 0) and (c % i ==0) and (d % i ) ==0:
#         print(i)
#         break