###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 11
sum_even = 0
i=0

# Calculate the sum of even numbers
while i !=N:
        i+=1
        if i % 2 == 0:
            sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")