try:
    a = input()
    f = open('b.txt','w',encoding='utf-8')
    f.write(str(a))
    f.close()
except Exception as e:
    print(e)