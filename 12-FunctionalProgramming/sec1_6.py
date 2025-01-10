km=int(input('enter speed:'))
h=int(input('enter hours:'))
m=int(input('enter minutes:'))
def avg_speed(distance,hours,minutes):
    return km/(h+(m/60))
result= avg_speed(km,h,m)
print(f'{result: .1f}')
