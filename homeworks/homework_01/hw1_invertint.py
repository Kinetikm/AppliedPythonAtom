#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    """
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    """
    i = 1
    if number < 0:
        number *= -1
        i *= -1
    n = 0
    while number > 0:
        n *= 10
        n += number % 10
        number = number // 10
    return n * i
