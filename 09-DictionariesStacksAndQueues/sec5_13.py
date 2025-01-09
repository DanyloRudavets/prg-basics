def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # If token is a number, push to stack
            stack.append(float(token))
        elif token in "+-*/":  # If token is an operator, pop two values and calculate
            if len(stack) < 2:
                return "Error: Insufficient values in the stack"
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return "Error: Division by zero"
                stack.append(a / b)
        elif token == '=':  # If token is '=', return the result
            if len(stack) == 1:
                return stack.pop()
            else:
                return "Error: Too many values in the stack"
        else:
            return f"Error: Invalid token '{token}'"

    return "Error: No '=' in the expression"

# Example usage
expression = "2 3 + ="
result = evaluate_rpn(expression)
print(f"Result of '{expression}': {result}")
