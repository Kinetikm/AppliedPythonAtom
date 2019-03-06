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
    num1 = type(x)
    num2 = type(y)
    if num1 == int or num1 == float or num1 == complex:
        if num2 == int or num2 == float or num2 == complex:
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
    else:
        return None
