#!/usr/bin/env python
# coding: utf-8


def reverse(number):  # режим говнокодера включен
    flag = '' if number > 0 else '-'
    return (int(flag + str(number)[::-1].lstrip('0').rstrip('-'))) \
        if number != 0 else 0
