a=0
b=0
k=10
c=0
def calc(a,b,k,c):
    for i in range (k-1):
        if i>1:
            c=a+b
            a=b
            b=c
        else:
            a=b+i
            b=a
    return c
