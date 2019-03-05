#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    t = 0
    number = str(number)
    if number[0] == '-':
        number = number[1:len(number)]
        number = '-' + number[::-1]
    else:
        number = number[::-1]
    return (int(number))
