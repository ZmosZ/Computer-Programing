def message():
    s = 0
    c = 0
    while(True):
        a = input()
        b = a.split(" ")
        if(b[0] == "-1"and b[1] == "-1"):
            break
        s = s+int(b[1])
        c = c + 1
    print(s/c)
message()