c='34352'
e=False
n=0
def calc(c,n,e):
    if e==True:
        for i in range(len(c)):
            if int(c[i])%2==0:
                n=n+int(c[i])
        return n
    else:
        for i in range(len(c)):
            if int(c[i])%2==1:
                n=n+int(c[i])
        return n