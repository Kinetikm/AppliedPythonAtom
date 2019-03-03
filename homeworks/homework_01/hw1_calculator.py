#!/usr/bin/env python
# coding: utf-8


def calculator(a, b, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if operator == "plus":
        return a + b
    if operator == "minus":
        return a - b
    if operator == "mult":
        return a * b
    if operator == "divide":
        return a / b if b != 0 else None
    return None
    raise NotImplementedError
