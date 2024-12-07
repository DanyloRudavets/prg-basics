a=[[7,3,7,9,0],
   [2,9,0,1,5],
   [3,8,6,4,7],
   [8,7,1,1,5]
   ]
c=0
for i in range(len(a)):
    if i==3:
        for j in range(len(a[i])):
            c+=a[i][j]
print(c)