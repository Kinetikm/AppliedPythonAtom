#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    a = input_string.lower()
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
