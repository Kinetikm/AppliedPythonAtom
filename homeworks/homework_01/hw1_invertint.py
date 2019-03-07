#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    neg = False
    if (number < 0):
        neg = True
        number = abs(number)
    n = number
    res = 0
    while n > 0:
        res = res*10 + (n % 10)
        n = n // 10
    if (neg):
        res = res * -1
    return res
    raise NotImplementedError
