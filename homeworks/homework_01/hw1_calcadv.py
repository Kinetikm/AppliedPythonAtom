#!/usr/bin/env python
# coding: utf-8

ops = set("*/+-")

def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    parts = input_string.split(' ')
    stack = list()
    for part in parts:
        if not part in ops:
            stack.append(float(part))
        elif len(stack)>1:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if part=='+':
                stack.append(a+b)
            elif part=='-':
                stack.append(a-b)
            elif part=='*':
                stack.append(a*b)
            elif part=='/' and b!=0:
                stack.append(a/b)
            else:
                return None
    if len(stack)==1:
        return stack[0]
    else:
        return None
