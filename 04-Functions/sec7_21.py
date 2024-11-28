def f(n1,n2,n3):
    if n1>n2 and n1>n3:
        if n2>n3:
            return n1-n3
        else: 
            return n1-n2
    elif n2>n1 and n2>n3:
        if n1>n3:
            return n2-n3
        else:
            return n2-n1
    elif n3>n1 and n3>n2:
        if n1>n2:
            return n3-n2
        else:
            return n3-n1
print(f(7,4,9))
print(f(2,12,8))
