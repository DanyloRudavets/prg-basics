
def le(a):
    c=[]
    c=a.split()
    return len(c)

def ord(a):
    a=a.split()
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if len(a[j])<len(a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
def alph(a):
    c=sorted(a.split())
    return c
