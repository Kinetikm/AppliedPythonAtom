#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    try:
        if (operator== 'plus'):
            return (x + y)
        if operator == "minus":
            return x - y
        if operator == "mult":
            return x * y
        if operator == 'divide':
            return (x / y)
        else:
            print('None')
    except:
        print('None')