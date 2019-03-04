#!/usr/bin/env python
# coding: utf-8


import numbers


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''

    operations = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'mult': lambda x, y: x * y,
        'divide': lambda x, y: divide(x, y),
    }
    try:
        if isinstance(x, numbers.Number) & isinstance(y, numbers.Number):
            if operator in operations.keys():
                return operations[operator](x, y)
            else:
                return None
    except TypeError:
        return None


def divide(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        return None
    except ValueError:
        return None
    return res
