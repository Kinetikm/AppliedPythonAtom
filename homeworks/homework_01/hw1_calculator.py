#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) != float or type(y) != float or type(operator) != str:
        return None
    if operator == 'plus':
        return int(x) + int(y)
    if operator == 'minus':
        return int(x) - int(y)
    if operator == 'mult':
        return int(x) * int(y)
    if operator == 'divide':
        return int(x) / int(y)
    else:
        return None

#
# a = input('Input x: ')
# b = input('Input y: ')
# op = input('Input operator: ')
# print(calculator(a, b, op))
