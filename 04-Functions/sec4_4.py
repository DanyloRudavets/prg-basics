###
# Calculates the sum of the digits in a number
#

def sum_digits(any_number):
    a=abs(any_number)
    b=str(a)
    c=0
    for i in range(len(b)):
        c=c+int(b[i])
    return c

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')