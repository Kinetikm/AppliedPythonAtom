#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    res = 0
    sign = -1 if number < 0 else 1
    number = abs(number)
    while(number):
        res = res * 10 + number % 10
        number //= 10
    return sign * res
