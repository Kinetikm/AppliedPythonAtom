#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    a = '()'
    b = '[]'
    c = '{}'
    s = input_string
    for i in range(len(input_string)):
        s = s.replace(a, '')
        s = s.replace(b, '')
        s = s.replace(c, '')
    if s == '':
        return True
    else:
        return False
