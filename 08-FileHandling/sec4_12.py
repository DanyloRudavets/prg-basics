import csv
file='books.csv'
with open(file, 'r')as originalfile:
    source=csv.reader(originalfile)
    next(source)
    for i in source:
        if i[2]=='Fantasy':
            with open('books_fantasy.txt', 'a')as file:
                write=csv.writer(file)
                write.writerow([i[0],i[1],i[3]])
        elif i[2]=='Historical':
            with open('books_historical.txt', 'a')as file:
                write=csv.writer(file)
                write.writerow([i[0],i[1],i[3]])
        if i[2]=='Romance':
            with open('books_romance.txt', 'a')as file:
                write=csv.writer(file)
                write.writerow([i[0],i[1],i[3]])
        elif i[2]=='Classic':
            with open('books_classic.txt', 'a')as file:
                write=csv.writer(file)
                write.writerow([i[0],i[1],i[3]])
