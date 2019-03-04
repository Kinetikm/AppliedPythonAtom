#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) not in [float, int, complex] \
            or type(y) not in [float, int, complex]:
        return None
    elif operator == 'plus':
        return x + y
    elif operator == 'minus':
        return x - y
    elif operator == 'mult':
        return x * y
    elif operator == 'divide' and y not in [0, 0.0, 0j]:
        return x / y
    else:
        return None
