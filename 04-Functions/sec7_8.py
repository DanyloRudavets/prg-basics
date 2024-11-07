c=0
b=0
g=0
def calc(a,c,b,g):
    if a>5:
        c=a//5
        b=(a-c*5)//2
        g=a-(5*c+b*2)
    else:
        b=a//2
        g=a-(5*c+b*2)
    return c,b,g
