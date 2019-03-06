#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    s2 = input_string[::-1]
    if input_string == s2:
        return True
    return False
