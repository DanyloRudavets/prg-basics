def f(d):
    maxd=1
    curc=1
    maxn=1
    for i in range(1,len(d)):
        if d[i]==d[i-1]:
            curc+=1
        else:
            if curc>maxd:
                maxd=curc
                maxn=int(d[i-1])
            curc=1
    if curc>maxd:
        maxn=int(d[i-1])
    return maxn
print(f("5233165554211"))
print(f("2133"))