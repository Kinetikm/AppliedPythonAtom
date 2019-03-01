#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    number_signum = 1 if number >= 0 else -1
    string_of_number = str(abs(number))
    string_of_number = string_of_number[::-1]
    return int(string_of_number) * number_signum
