###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
import math
pi=math.pi
r=int(input('enter radius:'))
c=2*pi*r
a=pi*r**2
print(f'Area: {a: .2f} circumference {c: .2f}')