#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number < 0:
        k = -1
    else:
        k = 1
    number = abs(number)
    n = 0
    while abs(number) > 0:
        ost = number % 10
        number = number // 10
        n = n * 10 + ost
    return k * n
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
