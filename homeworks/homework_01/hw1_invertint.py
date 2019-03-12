#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    tmp2 = []
    tmp1 = str(number)
    tmp3 = 0
    leng = len(tmp1)
    for i in range(leng):
        tmp2.append(tmp1[-(i + 1)])
    for i in range(leng):
        tmp3 += int(tmp1[i]) * (10 ** i)
    return tmp3


print(reverse(34567854))
