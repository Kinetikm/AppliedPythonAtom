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
    #if not (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
    if x is None or y is None:
        return None
    if type(x) is str or type(y) is str:
        return None
    if operator == "plus":
        return x + y
    if operator == "minus":
        return x - y
    if operator == "divide":
        if y != 0:
            return x / y
        else:
            return None
    if operator == "mult":
        return x * y 
    return None
    

    raise NotImplementedError

#print(calculator(140.28,140.28,'power'))
