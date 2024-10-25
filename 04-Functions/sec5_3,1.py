###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import sec5_3 # your own defined module

# Reads employee's data from keyboard
first_name = sec5_3.input_string('enter your name')
last_name = sec5_3.input_string('enter your surname')
age = sec5_3.input_integer('enter your age')
salary = sec5_3.input_real('enter your salary')
is_salary_hidden = sec5_3.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name:{first_name}', f'surname:{last_name}')
print(f'age:{age}')
if is_salary_hidden==True:
    print(f'Salary:{salary}')