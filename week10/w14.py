def bank():
    money = 0
    while(True):
        m = int(input())
        if m == 1:
            print(money)
        elif m ==2:
            t = int(input())
            money = money - t
            print(money)
        elif m == 3:
            t = int(input())
            money = money + t
            print(money)
        else:
            break
bank()