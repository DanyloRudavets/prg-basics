def f(x,y,d):
    for i in  range(x,y+1):
        if d in str(i):
            c=True
            break
        else:
            c=False
    return c
print(f(205,210,'04'))
print(f(10,15,'14'))
print(f(100,120,'11'))