#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    b = 0
    k = 1
    if number < 0:
        number = number * (-1)
        k = -1
    while number != 0:
        b *= 10
        b += (number % 10)
        number //= 10
    return b * k
    raise NotImplementedError
