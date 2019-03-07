#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    x = list(input_string)
    y = x.copy()
    for i in range(len(x)//2):
        y[i] = x[len(x)-1-i]
    print(x)
    print(y)
    if x == y:
        return True
    else:
        return False
