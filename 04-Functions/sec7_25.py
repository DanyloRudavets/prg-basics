def f(x,y):
    c=0
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and i%4!=0:
            c+=i
    return c
print(f(10,30))