#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    reversed_number = 0
    if number >= 0:
        while number > 0:
            reversed_number = reversed_number*10
            digit = number % 10
            reversed_number = reversed_number + digit
            number = number // 10
    else:
        while abs(number) > 0:
            reversed_number = reversed_number*10
            digit = abs(number) % 10
            reversed_number = reversed_number+digit
            number = abs(number) // 10
        reversed_number = reversed_number * (-1)
    return reversed_number
