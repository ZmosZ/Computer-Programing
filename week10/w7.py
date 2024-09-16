r = int(input())
h = int(input())
def cylinder (r,h):
    f = 3.14*(r**2)*h
    return round(f,2)
print(cylinder(r,h))