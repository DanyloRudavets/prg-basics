###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1==True:
    bulbs_on += 1
if light_switch2==True:
    bulbs_on+=2
print(f'The amount of light bulbs turned on is {bulbs_on}')