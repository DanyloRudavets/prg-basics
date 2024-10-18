###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2

if temperature >= 35:
    print("It is extermely hot")
elif temperature >= 30 and temperature<35:
    print ('it is hot ')
elif temperature >=15 and temperature<30:
    print('it is warm')
elif temperature >=0 and temperature<15:
    print('it is cold')
else:
    print('frost')
