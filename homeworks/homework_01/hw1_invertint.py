#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if (number == 0):
        return 0

    is_negative = False
    if (number < 0):
        is_negative = True

    buf = list(str(abs(number)))
    buf.reverse()

    if (buf[0] == '0'):
        buf.remove('0')

    if is_negative:
        buf.insert(0, '-')

    return int(''.join(buf))