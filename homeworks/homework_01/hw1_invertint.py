#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    buf = 0
    K = number
    if number < 0:
        number *= -1;
    while number:
        buf = buf * 10 + number % 10
        number = number // 10
    if K < 0:
        return  buf * (-1)
    else:
        return buf

