def temperatur():
    n = int(input())
    t = int(input())
    if n ==1:
        return(1.80*t)+32
    elif n ==2 :
        return(t-32)/1.80
    elif n == 3:
        return t-273
    elif n ==4:
        return t+273
print(temperatur())