#!/usr/bin/env python
# coding: utf-8


def is_number(n):
    return (type(n) == int or type(n) == float)


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if (is_number(x) and is_number(y)):
        if (operator == "plus"):
            return x + y
        if (operator == "minus"):
            return x - y
        if (operator == "mult"):
            return x * y
        if (operator == "divide"):
            if (y != 0):
                return x / y
            else:
                return None
    return None
    raise NotImplementedError
