#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    result = 0
    number_copy = number
    while number:
        if number >= 0:
            result = result * 10 + number % 10
            number //= 10
        else:
            if number % 10 == 0:
                result = result * 10 + number % 10
            else:
                result = result * 10 + (10 - number % 10)
            number = (number + 10 - 1) // 10

    if number_copy >= 0:
        return result
    else:
        return -result
