#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    k = 1
    if number < 0:
        k = -1
        number = -number
    number1 = 0
    while not number == 0:
        ost = number % 10
        number = number // 10
        number1 = number1 * 10
        number1 = number1 + ost
    return number1*k
