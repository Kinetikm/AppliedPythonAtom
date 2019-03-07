#!/usr/bin/env python
# coding: utf-8
#  import re


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    print(input_string)
    #  if re.search('\^d+', input_string) is None: return None
#    if re.search('\^d', input_string) is None:
#        print("first number")
#        return None
    if input_string[0].isdigit() is False:
        print("first isn't number")
        return None
    operators = ['plus', 'minus', 'multiple', 'divide', '+', '-', '*', '/']
#    for x in operators:
#        if input_string.find(x) == -1: return None
    print(input_string)
    s = []
    for x in input_string:
        if x in operators:
            n = s[-2]
            k = s[-1]
            s.pop()
            s.pop()
            if x == 'plus' or x == '+':
                res = n + k
            elif x == 'minus' or x == '-':
                res = n - k
            elif x == 'multile' or x == '*':
                res = n * k
            elif x == 'devide' or x == '/':
                res = n / k
            else:
                raise ValueError("incorrect operation")
            s.append(res)
        else:
            s.append(float(x))
    print(s[0])
    return s[0]
