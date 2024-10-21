for i in range(1,31):
    if i%5==0 and i%3==0:
        print('Bingo')
        continue
    elif i%3==0:
        print('Three')
        continue
    elif i%5==0:
        print('Five')
        continue
        
    print(i)
        