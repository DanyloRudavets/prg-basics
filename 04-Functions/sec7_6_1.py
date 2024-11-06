import sec7_6
n=input('enter credit card number:')
if __name__=='__main__':
    print(f'{n[0:2]}{sec7_6.calc(n, sec7_6.a)}{n[len(n)-2:]}')