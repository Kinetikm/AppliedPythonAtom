#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    number = str(number)
    if number[0] == '-':
        number = number[1:]
        return -int(number[::-1])
    else:
        return int(number[::-1])
