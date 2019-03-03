#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    bl = 0
    tmp = str(number)
    if tmp[0] == '-':
        tmp = tmp[1:]
        bl = 1

    rev = ""
    for i in range(len(tmp), 0, -1):
        rev += tmp[i-1]

    if bl == 1:
        # tmp = '-' + tmp
        return -int(rev)

    return int(rev)
