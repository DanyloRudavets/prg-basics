x=-9
y=3
s=0
def calc(x,y,s):
    if y<0:
        for i in range(y,0):
            if i%2==0:
                s=s-i
    elif x<0:
        for i in range(x,0):
            if i%2==0:
                s=s-i
    return s
