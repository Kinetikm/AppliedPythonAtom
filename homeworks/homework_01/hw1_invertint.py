#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    number = str(number)
    number.strip("0")
    if number[0] == "-":
        number = number[1:]
        number = "-" + number[::-1]
    else:
        number = number[::-1]
    return int(number)

    raise NotImplementedError
