a=[[-38, 19],
    [5,40],
    [-7,11],
    [29,16]
    ]
max=a[0][0]
min=a[0][1]
for i in a:
    for j in i:
        if j>max:
            max=j
        elif j<min:
            min=j
print(max)
print(min)
k=0
p=0
for i in a:
    k+=1
    p=0
    for j in i:
        p+=1
        if j==max:
            print(f'Max:Row number {k}, column number {p}')
        elif j==min:
            print(f'Min:Row number {k}, column number {p}')
