a=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]
   ]
c=0
for i in range (len(a)):

    g=i+1
    print(g, end=' ')
    for j in range(len(a[i])-1):
        c=j+2
        k=c*g
        print(k, end=' ')
    print()