#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if int(number) < 0:
        number = str(number).strip('-')
        number = str(number)[::-1]
        return int('-' + number)
    else:
        number = str(number)[::-1]
        return int(number)
