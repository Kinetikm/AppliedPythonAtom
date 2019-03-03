#!/usr/bin/env python
# coding: utf-8
'''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
 '''


def reverse(number):
    if number < 0:
        number = - number
        return - int(str(number)[::-1])
    else:
        return int(str(number)[::-1])
