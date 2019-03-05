#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    str_int = str(number)
    if (str_int[0] == '-'):
        return int('{}{}'.format('-', str_int[:0:-1]))
    else:
        return int(str_int[::-1])

    raise NotImplementedError
