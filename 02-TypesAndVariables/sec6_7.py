###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Danylo' # replace John with your name
for i in range(len(name)):
    print(f'The letter {name[i]} has a code {ord(name[i])}')
    
