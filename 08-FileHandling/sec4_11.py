file='powers.txt'
with open(file,'w')as file:
    for i in range(1,101):
        file.write(f'{i**1},{i**2},{i**3}\n')