#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    a = 1
    if number < 0:
        a = -1
        number = -number
    number1 = 0
    ost = 0
    while ost == 0:
        ost = number % 10
        number = number // 10
        number1 = number1 * 10
        number1 = number1 + ost
    return number1 * a
    raise NotImplementedError
