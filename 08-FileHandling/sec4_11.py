# file='powers.txt'
# with open(file,'w')as file:
#     for i in range(1,101):
#         file.write(f'{i**1},{i**2},{i**3}\n')
import csv
file='powertable.csv'
with open(file, 'w') as file:

    # field=['power of one','power of two','power of three']
    # write=csv.DictWriter(file, fieldnames=field)
    # write.writeheader()
    # for i in range(1,101):
    #     row={
    #         'power of one': i**1,
    #         'power of two': i**2,
    #         'power of three': i**3
    #    }
    #     write.writerow(row)
    write=csv.writer(file)
    for i in range(1,101):

       write.writerow([i**1,i**2,i**3])
