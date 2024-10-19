d=int(input('enter a decimal number:'))
q=''
while d!=0:
    if d%2==0:
        q=q+'1'
    else:
        q=q+'0'
    d//=2
print(q)