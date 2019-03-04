#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    buf = 0
    while number:
        buf=buf*10 + number % 10
        number /= 10
    return buf
