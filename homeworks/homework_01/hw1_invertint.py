#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if number != 0:
        sign = abs(number) / number
        number = str(abs(number))
        number = number[::-1]
        while (number[0] == 0) and (len(number) > 1):
            number = number[1:]
        return int(number)*int(sign)
    else:
        return 0
    raise NotImplementedError
