#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    k = 1
    if number < 0:
        k = -1
        number = number * (-1)
    s1 = str(number)
    s2 = s1[::-1]
    return(k*int(s2))
