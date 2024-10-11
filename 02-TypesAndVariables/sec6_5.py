###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
if len(phone)!=9:
    print(False)
else:
    p=phone.strip()
    print(p)