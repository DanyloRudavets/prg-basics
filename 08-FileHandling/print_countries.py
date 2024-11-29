###
# Reads from file, line by line
#
n=1
with open("countries.txt" , 'r') as file:
    for line in file:
        print(n, line, end="")
        n+=1