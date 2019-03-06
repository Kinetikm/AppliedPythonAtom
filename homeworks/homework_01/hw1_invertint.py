#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if not (isinstance(number, int)):
        return None
    if number == 0:
        return 0
    sign = 1
    if number < 0:
        sign = -1
        number = number * (-1)
    newstr = str(number)[::-1]
    for ch in newstr:
        if ch != '0':
            break
        else:
            newstr = newstr[1::1]
    return int(newstr) * sign
