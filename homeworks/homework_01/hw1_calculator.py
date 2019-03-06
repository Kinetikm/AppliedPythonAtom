#!/usr/bin/env pythonoppror
# coding: utf-8


def calculator(x, y, operator):
    try:
        x = float(x)
        y = float(y)
        result = None
        if operator == 'plus':
            result = x + y
        if operator == 'minus':
            result = x - y
        if operator == 'mult':
            result = x * y
        if operator == 'divide':
            result = x / y
        return result
    except TypeError:
        return None
    except ZeroDivisionError:
        return None
    except ValueError:
        return None
