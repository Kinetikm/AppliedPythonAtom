#!/usr/bin/env python
# coding: utf-8


def sgn(a):
    if a >= 0:
        return 1
    return -1


def reverse(number):
    n = 0
    number2 = abs(number)
    while number2:
        n *= 10
        n += number2 % 10
        number2 //= 10
    n *= sgn(number)
    return n
    raise NotImplementedError
