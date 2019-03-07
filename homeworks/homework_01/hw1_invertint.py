#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    number = str(number)
    if number[0] == '-':
        number = int(number[:0:-1]) * -1
        return number
    else:
        return int(number[::-1])
