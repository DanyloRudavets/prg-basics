a=0
q=''
while len(q)!=4 or a>3:
    a+=1
    if a<4:
        q=input('Enter your password')
    else:
        print('Your card is blocked')
        break
