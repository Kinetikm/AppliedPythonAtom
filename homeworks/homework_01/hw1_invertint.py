#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number == 0:
        return number
    i = 1
    if number < 0:
        i = -1
        number *= i
    while (number % 10) == 0:
        number /= 10
    number = str(int(number))
    number = int(number[::-1])
    return i*number
