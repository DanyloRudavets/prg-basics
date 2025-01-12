n=[(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
def f(n):
    r=[]
    for i in n:
        s=sum(i)
        mn=min(i)
        mx=max(i)
        r.append(s-mn-mx)
    return r
print(f(n))




