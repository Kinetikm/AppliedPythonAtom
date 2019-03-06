#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if (type(x) in [float, int]) and (type(y) in [float, int]):
        if (operator in ['plus', "+"]):
            return (x + y)
        elif operator in ["minus", "-"]:
            return x - y
        elif operator in ["mult", "*"]:
            return x * y
        elif operator in ['divide', "/"]:
            if y != 0:
                return (x / y)
            else:
                return (None)
        else:
            return (None)
    else:
        return (None)
