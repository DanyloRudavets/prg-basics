###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Enter your swift code: ')
print(f'Bank Code: {swift[:4]}')
print(f'Country Code:{swift[4:6]} ')
print(f'Location Code:{swift[6:8]}')
print(f'Branch Code: {swift[8:]}')