d=int(input('enter a decimal number:'))
q=''
while d!=0:
   # if d%2==0:
   #     q='0'+q
   # else:
    #     q='1'+q
    q=str(d%2) + q
    d//=2

print(q)
print(124//2)

