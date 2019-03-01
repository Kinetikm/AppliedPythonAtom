#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    sgn = 1 if number >= 0 else -1
    return int(str(abs(number))[::-1]) * sgn
