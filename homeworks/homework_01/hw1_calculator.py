#!/usr/bin/env python
# coding: utf-8


def type_check(a):
    if (type(a) is int) or (type(a) is float):
        return True
    else:
        return False


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if type_check(x) and type_check(y):
        if operator == "plus":
            return x + y
        if operator == "minus":
            return x - y
        if operator == "mult":
            return x * y
        if operator == "divide":
            if y != 0:
                return x / y
            else:
                return None
    return None
    raise NotImplementedError
