d=0.25
a=int(input('enter amount'))
p=int(input('enter a price'))
if a >2 :
    print(2*p+(a-2)*p*(1-d))
else:
    print(a*p)