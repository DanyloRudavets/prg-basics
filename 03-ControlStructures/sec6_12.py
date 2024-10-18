car_speed=int(input('enter a car speed:'))
speed_limit_min=40
speed_limit_max=140
if car_speed<speed_limit_min or  car_speed>speed_limit_max:
    print('invalid car speed ')