def f(n):
    l=[]
    n=str(n)
    for i in n:
        if int(i)%2!=0:
            l.append(int(i))
    if  len(l)==0:
        return -1
    else:
        return max(l)-min(l)
print(f(10852))
print(f(723597))
print(f(4388))
print(f(846206))