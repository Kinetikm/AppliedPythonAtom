#!/usr/bin/env python
# coding: utf-8

operations = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "mult": lambda x, y: x * y,
    "divide": lambda x, y: x / y
}


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''

    try:
        x, y = float(x), float(y)
    except (TypeError, ValueError):
        return None
    try:
        return operations[operator](x, y)
    except (KeyError, ZeroDivisionError):
        return None
