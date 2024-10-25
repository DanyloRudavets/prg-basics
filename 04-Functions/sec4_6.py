###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    if day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    if day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    if day_number == 7:
        result = 'Sunday'

    return result

# Function usage
print('The name of day 1 in the week is', day_name(1))
print('The name of day 2 in the week is', day_name(2))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 4 in the week is', day_name(4))
print('The name of day 5 in the week is', day_name(5))
print('The name of day 6 in the week is', day_name(6))
print('The name of day 7 in the week is', day_name(7))