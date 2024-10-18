###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M medium size')
elif size== 'L':
    print('l large size')
else:
    print('Xl size is extra large')