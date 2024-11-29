sq=[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

k=0
for i in range(len(sq)):
        if 1 in sq[i]:
            k=sq[i].index(1)+1
        else:
            sq[i][k]=1
            k=sq[i].index(1)+1
print(sq)