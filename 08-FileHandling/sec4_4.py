file='it_company.csv'
try:
    with open(file, 'r') as file:
        content=file.read()
        li=str(content).split('\n')
    k=0
    i=input('Press Enter..(0 to stop)')
    while i!=0:
        if i=='':
            for i in range(5):
                print(li[k], '\n')
                k+=1
            i=input('Press Enter..(0 to stop)')
except IndexError:
    print('Don\'t have any other people left')
        
