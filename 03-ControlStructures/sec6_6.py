a= int(input('enter your age:'))
if a>0 and a<13:
    print('child')
elif a>=13 and a<=19:
    print('teenager')
elif a> 19 and a<=64:
    print('adult')
else:
    print('senior')