#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number < 0:
        minus = 1
    else:
        minus = 0  
    number = list(str(abs(number)))
    number.reverse()
    while number[0] == '0':
        number.pop(0)
    h = number[0]
    i = 1
    while i < len(number):
        h += number[i]
        i += 1
        
    number = int(h)
    if minus:
        number *= -1
    return number
    raise NotImplementedError
