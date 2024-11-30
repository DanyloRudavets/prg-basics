def sb(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    for i in range(len(n)-1,0,-1):
        if n[i]!=n[i-1]:
            break
    return n[i-1]
def b_l(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    c=n[len(n)-1]-n[0]
    return c   
def med(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n[len(n)//2]
def minmax(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n[0],n[-1]
def split(n):
    c=''
    for i in range(len(n)):
        c=c+str(n[i])+'-'
    return c[:-1]
        

