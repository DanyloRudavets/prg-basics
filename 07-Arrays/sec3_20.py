a=[7,9,2,4,5,6]
k=[]
c=[]
for i in a:
    if i%2==0:
        k.append(i)
    else:
        c.append(i)
print(k+c)
