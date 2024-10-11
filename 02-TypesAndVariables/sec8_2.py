###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# ...
# ...
# ...
c=int(input('enter temperature in celsius:'))
f=(c-32) * 5/9
k=c+273.15
print(f''' Temperature in fahrenheit: {f: .2f}
      Temperature in kelvin: {k: .2f}''')