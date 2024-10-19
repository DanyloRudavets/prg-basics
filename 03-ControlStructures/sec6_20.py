a=int(input('enter the amount in PLN'))
q=0
c=0
f=a%5
if f==0:
    q=a//5
    print(f'5 PLN coins:{q}')
elif f!=0:
    q=a//5
    print(f'5 PLN coins:{q}')
    if f%2==0:
        c=f//2
        q=q+c
        print(f'2 Pln coins:{c}')
    else:
        c=f//2
        q=q+c+1
        print(f'2 Pln coins:{c}')
        print('1 Pln coins: 1')

