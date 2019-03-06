#!/usr/bin/env python
# coding: utf-8

def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    print(number)
    a = number
    b = str(a)
    mas = []
    invert = ''
    if b[0] == '-':
        mas.append(b[0])
    if len(mas) == 0:
        for i in reversed(range(len(b))):
            mas.append(b[i])
    else:
        for i in reversed(range(1, len(b))):
            mas.append(b[i])
    for i in mas:
        invert += i
    return int(invert)

