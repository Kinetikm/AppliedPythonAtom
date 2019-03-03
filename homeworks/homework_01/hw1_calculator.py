#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    try:
        if operator == 'plus':
            return float(x) + float(y)
        elif operator == 'minus':
            return float(x) - float(y)
        elif operator == 'mult':
            return float(x) * float(y)
        elif operator == 'divide':
            if y == 0:
                return None
            else:
                return float(x) / float(y)
        else:
            return None
    except Exception:
        return None

    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    # raise NotImplementedError
