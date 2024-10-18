###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('enter a number'))
number2 = int(input ('enter a number'))
operator = input('enter an operator')
if operator=='+':
    print(number1+number2)
elif operator=='-':
    print(number1-number2)
elif operator=='*':
    print(number1*number2)
elif operator=='/':
    print(number1/number2)