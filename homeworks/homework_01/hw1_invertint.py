#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number < 0:
        number = abs(number)
        s = str(number)[::-1]
        number = -int(s)
    else:
        s = str(number)[::-1]
        number = int(s)
    return number
    raise NotImplementedError