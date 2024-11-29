a=[2,3,2,5,8,1,9,8]
for i in a:
    n=a.count(i)
    if n>1:
        c=a.index(i)
        a.remove(a[c])
        print(i)
        print(c)
print(a)