import csv
file='it_company.csv'
print('GRAPHIC DESIGNERS')
print(20*'=')
with open(file, 'r')as file:
    read=csv.reader(file)
    next(read)
    for i in read:
        print(f'{i[0]} {i[1]},{i[3]}')