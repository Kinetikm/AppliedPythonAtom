#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    try:
        int(x)
        int(y)
        if operator == "plus":
            res = x+y
        elif operator == "minus":
            res = x-y
        elif operator == "mult":
            res = x*y
        elif operator == "divide":
            if (y == 0):
                return (None)
            else:
                res = x/y
        else:
            return (None)
        return (res)
    except:
        return(None)
