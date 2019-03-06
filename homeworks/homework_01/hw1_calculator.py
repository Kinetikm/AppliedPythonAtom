#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if (type(x) == float or type(x) == int) and\
            (type(y) == float or type(y) == int):
        if operator == 'plus':
            return float(x) + float(y)
        if operator == 'minus':
            return float(x) - float(y)
        if operator == 'mult':
            return float(x) * float(y)
        if operator == 'divide':
            return float(x) / float(y)
        else:
            return None
