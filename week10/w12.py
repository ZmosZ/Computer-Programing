def interest():
    m =int(input())
    i =int(input())
    y =int(input())
    
    for j in range(y):
        m = m+(m*(i/100))
    return m
print(interest())