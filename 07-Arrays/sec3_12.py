a=[2,3,2,5,8,1,9,8,2]
c=[]
for i in a:
    n=a.count(i)
    if n>1:
        c.append(i)
for i in c:
    a.remove(i)

print(a)