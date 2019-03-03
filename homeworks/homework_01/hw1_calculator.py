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
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        if operator == 'plus':
            return x + y
        elif operator == 'minus':
            return x - y
        elif operator == 'mult':
            return x * y
        elif operator == 'divide' and y != 0:
            return x / y
        return
    return
    raise NotImplementedError
