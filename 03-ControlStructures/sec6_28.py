print('the fibonacci sequance:')
f=0
s=1
sum=0
t=20
c=0
while c<t:
    sum=f+s
    f=s
    s=sum
    c+=1
    print(sum)