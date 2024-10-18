x=int(input('enter x coordinate:'))
y=int(input('enter y coordinate:'))
if x>0:
    if y>0:
        print(f'Point P({x},{y}) is located in the first quadrant of the coordinate system')
    elif y<0:
        print(f'Point P({x},{y}) is located in the forth quadrant of the coordinate system')
    if y==0:
        print(f'Point P({x},{y}) belongs to y-axis')
if x<0:
    if y>0:
        print(f'Point P({x},{y}) is located in the second quadrant of the coordinate system')
    elif y<0:
        print(f'Point P({x},{y}) is located in the third quadrant of the coordinate system')
    if y==0:
        print(f'Point P({x},{y}) belongs to y-axis')
if x==0:
    if y==0:
        print(f'Point P({x},{y}) belongs to origin')
    elif y>0 or y<0:
        print(f'Point P({x},{y}) belongs to x-axis')
