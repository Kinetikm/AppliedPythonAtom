#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    ret = 0
    sign = 1
    if number < 0:
        number = number * (-1)
        sign = -1
    while number != 0:
        dig = number % 10
        number = number // 10
        ret = ret * 10
        ret = ret + dig
    return ret * sign
