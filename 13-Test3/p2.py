def f(x,y,d):
    c=0
    for i in range(x,y+1):
        if str(d) in str(i):
            print(i)
            c+=str(i).count(str(d))
    return c
print(f(10,15,1))
