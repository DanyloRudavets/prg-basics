###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('enter last letter:')
first_letter_code = ord(first)
last_letter=ord(last)
number_of_letters =last_letter-first_letter_code
print(f'Between {first} and {last} is {number_of_letters} letters')