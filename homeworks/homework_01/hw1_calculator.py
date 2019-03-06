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
        if x.isdigit() & y.isdigit():
        c=float(x)
        d=float(y)
        if operator == "plus":
            return c+d
        if operator == "minus":
            return c-d
        if operator == "divide":
            return c/d
        if operator == "mult":
            return c*d
    raise print("None") 
    raise NotImplementedError 