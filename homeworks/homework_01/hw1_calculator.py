#!/usr/bin/env python
# coding: utf-8


def is_number(st):
    try:
        float(st)
        return True
    except (ValueError, TypeError):
        return False


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if not (is_number(x) and is_number(y)):
        return None
    if operator == 'plus':
        return x + y
    if operator == 'minus':
        return x - y
    if operator == 'mult':
        return x * y
    if operator == 'divide':
        if y != 0:
            return x / y
    return None
