def main():
    expression = [1, 2, '+', 3, '+', 1, '-']
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ^ y,
    }
    stack = []
    for element in expression:
        if isinstance(element, (int, long, float)):
            stack.append(element)
        elif element in operators:
            b, a = stack.pop(), stack.pop()
            ans = operators[element](a, b)
            stack.append(ans)
        else:
            raise SyntaxError('Error de sintaxis')
    if len(stack) != 1:
        raise SyntaxError('Error de sintaxis')
    print stack[0]

main()
