#not finished 

n=int(input('enter a number:'))
q=0
for i in range (2,n+1):
    for h in range(1,i+1):
        if i/h==True:
            q+=1
            if q==2:
                print(i)

    