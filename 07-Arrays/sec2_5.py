# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
s=0
a=0
def seats_total():
   s=0
   for i in cinema_seats:
      for j in i:
         s+=1
   return s
def seats_available():
   a=0
   for i in cinema_seats:
      a +=i.count("A")
   return a

def seats_booked():
   b=0
   for i in cinema_seats:
      b +=i.count("B")
   return b

def seat_status(row, place):
   c=False
   if cinema_seats[row-1][place-1]=="A":
      c=True

   return c

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total())
print('Seats available:', seats_available())
print('Seats booked:', seats_booked())
print('Seat in row 1, place 1:', seat_status(1,1))
print('Seat in row 5, place 5:', seat_status(5,5))
print('Seat in row 3, place 5:', seat_status(3,5))