#not finished 
q=True
n=100
h=''
for i in range (2,n):
    q=True
    for j in range(2,i):
        if i%j==0:
            q=False
    if q:   
         print(i, end=' ')
        