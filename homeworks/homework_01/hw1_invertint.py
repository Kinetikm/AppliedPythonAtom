#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    sign = -1 if number < 0 else 1
    number = abs(number)
    listOfDigits = [int(digit) for digit in str(number)]
    listOfDigits.reverse()
    return sign * int("".join(map(str, listOfDigits)))
