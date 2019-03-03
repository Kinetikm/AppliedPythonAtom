#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    """
    Метод, принимающий
    на вход
    int и
    возвращающий
    инвертированный
    int
    :param number:
     исходное число
    :return:
    инвертированное число
    """

    if number < 0:
        k = -1
    else:
        k = 1
    number = abs(number)
    a = 0
    while abs(number) > 0:
        l1 = number % 10
        number = number // 10
        a = a * 10 + l1
    return k * a
    raise NotImplementedError

