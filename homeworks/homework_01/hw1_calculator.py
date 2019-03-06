#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    # print(x,y,operator)
    exeption = {str, None, ''}

    if type(x) in exeption:
        return None
    if type(y) in exeption:
        return None
    if y is None:
        return None
    if x is None:
        return None

    elif operator == 'plus':
        return x + y
    elif operator == 'minus':
        return x - y
    elif operator == 'mult':
        return x * y
    elif operator == 'divide':
        if y == 0:
            return None
        else:
            return x / y
