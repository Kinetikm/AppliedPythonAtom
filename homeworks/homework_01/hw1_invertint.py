#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    fl = False
    number = str(number)
    if number[0] == '-':
        fl = True
        number = number.replace('-', '')
        print(number)
    if number.isdigit():
        if (number != '0'):
            val = int(number.rstrip("0")[::-1])
            if fl:
                val = -val
            return val
        else:
            return 0
