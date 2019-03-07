#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number < 0:
        return int('-' + str(number).strip('-')[::-1])
    elif number == 0:
        return 0
    else:
        return int(str(number)[::-1])
