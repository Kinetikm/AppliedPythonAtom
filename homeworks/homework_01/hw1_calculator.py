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
    if (type(a)==int or type(a)==float):
        if (type(b)==int or type(b)==float):
            if operator == "plus":
                return a+b
            if operator == "minus":
                return a-b
            if operator == "divide":
                return a/b
            if operator == "mult":
                return a*b
    raise print("None") 