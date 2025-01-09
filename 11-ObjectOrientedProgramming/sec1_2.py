class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def per(self):
      return self.a*4

   
square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {Square.area(square1)}, Perimeter is  {Square.per(square1)}')
print ('Square with side 6:')
print(f' {Square.area(square2)} {Square.per(square2)}')