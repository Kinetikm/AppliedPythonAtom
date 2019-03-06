def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    split_string = input_string.split(' ')
    
    stack = []
    for i in split_string:
        if i == '+' and len(stack) >= 2:
            result = float(stack.pop()) + float(stack.pop())
            stack.append(result)
        elif i == '*':
            result = float(stack.pop()) * float(stack.pop())
            stack.append(result)
        elif i == '-':
            result = float(stack.pop()) - float(stack.pop())
            stack.append(result)
        elif i == '/':
            result = float(stack.pop()) / float(stack.pop())
            stack.append(result)
        else:
            stack.append(i)

    return stack[0]
    raise NotImplementedError



