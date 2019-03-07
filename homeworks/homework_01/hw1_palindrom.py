#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    print("STR: ", input_string)
    length = len(input_string)
    a = input_string[:length//2]
    b = input_string[length // 2 + length % 2:]
    b = b[::-1]
    print(a, b)
    if a == b:
        return True
    else:
        return False
