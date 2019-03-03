#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    myNumber = 0
    while number > 0:
        myNumber *= 10
        myNumber += (number % 10)
        number //= 10
    return myNumber
    raise NotImplementedError
