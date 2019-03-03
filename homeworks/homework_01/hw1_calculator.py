#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if operator == "plus":
        return x+y
    if operator == "minus":
        return x-y
    if operator == "divide":
        if y != 0:
            return None
        else:
            return x/y
    if operator == "mult":
        return x*y
    raise NotImplementedError
