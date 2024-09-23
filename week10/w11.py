from math import *
def Calculator():
    A= []
    n = int(input())
    for i in range(n):
        t = int(input())
        A.append(t)
    m = int (input())
    avg = sum(A)/len(A)
    ss = 0
    for i in A:
        ss = ss + (i-avg)**2
    sd = sqrt(ss)/n
    if m == 1:
        print(avg)
    elif m == 2 :
        A.sort()
        print(A[(len(A)-1)//2])
    elif m == 3:
        L =0
        t =0
        for i in range (len(A)):
            c = A.count(A[i])
            if c > L:
                L = c
                mode = A[i]
        print(mode)
    elif m ==4:
        print(sd)
    elif m == 5:
        for i in A:
            print((i-avg)/sd)
Calculator()