#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    print(input_string)
    a = input_string
    a2 = ''
    for j in a:
        a2 = a2 + j
    s = ''
    for i in reversed(range(len(a2))):
        s += a2[i]
    print(a2, s)
    if a2 == s:
        return True
    else:
        return False
