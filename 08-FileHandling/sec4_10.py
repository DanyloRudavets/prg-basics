file='clothing.csv'
import csv
with open(file, 'r')as file:
    read=csv.reader(file)
    next(read)
    for i in read:
        if float(i[5])<60 and int(i[6])<40:
            print(i[1])