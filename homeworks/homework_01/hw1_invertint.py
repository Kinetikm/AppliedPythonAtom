#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if (number[0] == "+")or(number[0] == "-") :
        a = number[0]
        b = number[len(number):0:-1]
        return int(a+b)
    else: return  int(number[::-1])