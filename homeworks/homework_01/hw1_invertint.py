#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    negative_number = False
    if number < 0:
        negative_number = True
        number = -1 * number
    number_in_string = str(number)
    number_in_string = number_in_string[::-1]
    new_number = int(number_in_string)
    if negative_number:
        return -1 * new_number
    else:
        return new_number
