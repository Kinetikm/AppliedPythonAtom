#!/usr/bin/env python
# coding: utf-8
import math


def reverse(number):
    if number == 0:
        return 0
    num1 = int(number)

    if num1 < 0:
        minus = True
    else:
        minus = False

    unsigned_num = int(math.fabs(num1))

    str_num = str(unsigned_num)

    str1 = str_num.strip('0')

    str2 = str1[::-1]
    if minus:
        str3 = "-" + str2
        str4 = int(str3)
    else:
        str4 = int(str2)
    return str4

    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    # raise NotImplementedError
