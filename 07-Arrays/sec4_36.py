k=[]
c=0
m=[[2,1],
   [3,5],
   [7,4],
   [2,6]]
for i in m:
    c+=1
if c>1:
    for i in m:
        for j in i:
            k.append(j)
    print(k)
else:
    print(m)
