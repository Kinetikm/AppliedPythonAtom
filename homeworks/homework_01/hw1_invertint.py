#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    flag = False
    if number < 0:
        flag = True
        number = -number
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10
    if flag:
        result = -result
    return result
