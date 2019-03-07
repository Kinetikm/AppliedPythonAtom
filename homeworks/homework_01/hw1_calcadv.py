#!/usr/bin/env python
# coding: utf-8


import operator

OPERATORS = {
    '+': operator.add, 
    '-': operator.sub, 
    '*': operator.mul, 
    '/': operator.truediv
}

def calc(string):
    if set('[~!@#$%^&_{}";\'\n]').intersection(string):
        return None
    stack = [0]
    for token in string.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()