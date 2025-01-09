import csv
import re
filep='province.csv'
filel='vehicle.txt'
with open(filep,'r', encoding='utf-8')as filep:
    read1=csv.reader(filep)
    d={}
    next(read1)
    for i in read1:
        d.update({i[0]:0})
    print(d)
        
patern='(^[A-Z]{1})'
with open(filel,'r')as filel:
    read2=filel.read()
    c=re.findall(patern,i)

