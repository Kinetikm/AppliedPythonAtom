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
    if  type(x) == str or type(y)==str:
        return None
    elif  x == None or y==None:
        return None
    if operator in ('plus', 'minus', 'mult', 'divide'):
        if operator == 'plus':
            return x+y
        elif operator == 'minus':
            return x-y
        elif operator == 'mult':
            return x*y
        elif operator == 'divide':
            if y != 0:
                return x/y
            return None
    else:
        return None
    raise NotImplementedError
