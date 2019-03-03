#!/usr/bin/env python
# coding: utf-8

def reverse(number):
    '''
    Метод, принимающий на вход
    int и     возвращающий
    инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    ost = 0
    if number < 0:
        number = -number
        while ost == 0:
            ost = number % 10
            number = number/10
        number = number*10
        st = str(int(number))
        st = st[::-1]
        a = int(st)
        return -a
    else:
        while ost == 0:
            ost = number % 10
            number = number / 10
        number = number * 10
        st = str(int(number))
        st = st[::-1]
        a = int(st)
        return a
    raise NotImplementedError

