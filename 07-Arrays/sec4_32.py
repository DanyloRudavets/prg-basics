a=[[7,3,7,9,0],
   [2,9,0,1,5],
   [3,8,6,4,7],
   ]
c=[]
g=[]
for i in range(len(a)):
    k=a
    if i==0:
        for j in k[i]:
            c.append(j)
        k.pop(i)
        k.append(c)
    elif i==2:
        for j in a[1]:
            g.append(j)
        k.pop(i-1)
        k.insert(0,g)
print(k)
# a = [
#     [7, 3, 7, 9, 0], 
#     [2, 9, 0, 1, 5],
#     [3, 8, 6, 4, 7],
# ]

# # Swap the first and second rows
# a[0], a[1] = a[1], a[0]

# # Print the result
# print(a)
