#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    s = str(number)
    if s == '':
        return None
    n = 0
    if number < 0:
        n = -1
    else:
        n = 1
    return n * int(s[::-1].strip("-"))
