#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number >= 0:
        return int(str(number)[::-1])
    else:
        return int(str(number * - 1)[::-1]) * - 1

#    '''
#    Метод, принимающий на вход int и
#    возвращающий инвертированный int
#    :param number: исходное число
#    :return: инвертированное число
#    '''
