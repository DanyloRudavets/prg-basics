###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
a1=int(a)
b= int(input('b='))
c= int(input('c='))
v=a1*b*c
f=a1*b+b*c+c*a1
sa=2*f
print(f'volume {v}')
print(f'surface area {sa}')