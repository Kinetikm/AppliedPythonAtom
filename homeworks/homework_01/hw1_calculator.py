#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    """
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    """
    if operator == 'plus':
        try:
            return x + y
        except TypeError:
            return None
    elif operator == 'minus':
        try:
            return x - y
        except TypeError:
            return None
    elif operator == 'mult':
        try:
            return x * y
        except TypeError:
            return None
    elif operator == 'divide':
        if x == 0:
            return None
        try:
            return x / y
        except TypeError:
            return None
