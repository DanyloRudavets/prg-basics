n=input('Enter EAN-13 article number:')
if len(n)==13 and n.isdigit()==True:
    print('The number is correct')
    if '590' in n[:3]:
        print('This product was made in Poland')