import math
def triangle_area(a,b,c):
   s=(a+b+c)//2
   q=math.sqrt(s*(s-a)*(s-b)*(s-c))
   return q
print(triangle_area(3,4,5))