#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    a = 1
    if number < 0:
        a = -1
    number = number * a
    
    s =str(number)
    s1 = s[::-1]
    return int(s1)*a

    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    raise NotImplementedError
