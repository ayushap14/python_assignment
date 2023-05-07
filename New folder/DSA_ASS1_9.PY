def evaluate_postfix_expression(expression: str) -> int:
    stack = []
    for element in expression:
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == '+':
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2
            else:
                raise ValueError('Invalid operator')
            stack.append(result)
    return stack.pop()
