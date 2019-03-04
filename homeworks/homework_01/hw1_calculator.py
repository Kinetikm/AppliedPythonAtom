#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if isinstance(x, (int, float)) * isinstance(y, (int, float)) == 1:
        if operator == 'plus':
            return x + y
        elif operator == 'minus':
            return x - y
        elif operator == 'mult':
            return x * y
        elif operator == 'divide' and y != float(0):
            return x / y
        else:
            return None
    else:
        return None
    raise NotImplementedError
