#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    ind = False
    myNumber = 0
    if number < 0:
        number *= -1
        ind = True
    while number > 0:
        myNumber *= 10
        myNumber += (number % 10)
        number //= 10
    if ind:
        return -1*myNumber
    else:
        return myNumber
