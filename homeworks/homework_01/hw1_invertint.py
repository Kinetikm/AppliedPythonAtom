#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    res=0
    while number>0:
        remainder = number%10
        number = int(number/10)
        res = res*10+remainder;
    return res