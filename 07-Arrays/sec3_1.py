n=[34,7,19,21,8]
i=0
c=0
while i!=len(n)+1:
    if n[i-1]%2==0:
        c+=1
    i+=1
print(c)
