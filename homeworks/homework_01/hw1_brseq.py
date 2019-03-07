#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    b_op = ('(', '[', '{')
    b_cl = (')', ']', '}')
    stack = []
    for sym in input_string:
        if sym in b_op:
            stack.append(sym)
        if sym in b_cl:
            if len(stack) == 0:
                return False
            index = b_cl.index(sym)
            op_br = b_op[index]
            if stack[-1] == op_br:
                stack = stack[:-1]
            else:
                return False
    return not stack
