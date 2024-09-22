def my_message():
    num = int(input())
    s = 0
    c = 0
    for i in range (num):
        a = input()
        b = a.split(" ")
        s = s+int(b[1])
        c = c + 1
    print(s/c)
my_message()