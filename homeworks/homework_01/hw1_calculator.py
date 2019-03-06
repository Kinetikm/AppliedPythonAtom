#!/usr/bin/env python
# coding: utf-8

def calculator(x, y, operator):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if operator == "minus":
            return x - y
        if operator == "plus":
            return x + y
        if operator == "mult":
            return x * y
        if operator == "divide":
            return x / y
        else:
            return None
    else:
        return None